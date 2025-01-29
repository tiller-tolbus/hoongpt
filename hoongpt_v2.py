#!/usr/bin/env python3

import json
import os
import re
import subprocess
import time
import sqlite3
from datetime import datetime
from typing import Dict, List, Optional, Tuple, Any
import requests
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Cost per 1K tokens (approximation)
COST_PER_1K_TOKENS = 0.01

def get_db():
    return sqlite3.connect('hoongpt.db')

class TestCase:
    def __init__(self, input_str: str, expected: str):
        self.input = input_str
        self.expected = expected

class TestFile:
    def __init__(self, question: str, tests: List[TestCase]):
        self.question = question
        self.tests = tests

class TestResult:
    def __init__(self, input_str: str, passed: bool, output: str, error: Optional[str] = None):
        self.input = input_str
        self.passed = passed
        self.output = output
        self.error = error

class TestResults:
    def __init__(self, hoon_code: str, results: List[TestResult]):
        self.hoon_code = hoon_code
        self.results = results

def verify_database():
    """Verify database integrity and schema."""
    conn = get_db()
    c = conn.cursor()
    
    try:
        c.execute("SELECT name FROM sqlite_master WHERE type='table'")
        tables = {row[0] for row in c.fetchall()}
        required_tables = {'runs', 'results', 'prompt_strategies', 'questions'}
        
        if not required_tables.issubset(tables):
            missing = required_tables - tables
            raise ValueError(f"Database missing required tables: {missing}")
            
        c.execute('PRAGMA foreign_key_check')
        invalid_fks = c.fetchall()
        if invalid_fks:
            raise ValueError(f"Database has invalid foreign keys: {invalid_fks}")
            
        conn.close()
        return True
    except Exception as e:
        conn.close()
        raise e

def read_test_file(file_path: str) -> TestFile:
    """Read and parse a test file."""
    with open(file_path, 'r') as f:
        data = json.load(f)
        tests = [TestCase(t["input"], t["expected"]) for t in data["tests"]]
        return TestFile(data["question"], tests)

def query_ai_model(system_prompt: str, user_prompt: str) -> Tuple[str, Dict[str, int]]:
    """Query the OpenAI API for a response."""
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        raise ValueError("OPENAI_API_KEY environment variable not set")

    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }
    
    payload = {
        "model": "gpt-4-turbo",
        "messages": [
            {
                "role": "system",
                "content": system_prompt
            },
            {
                "role": "user",
                "content": user_prompt
            }
        ]
    }

    response = requests.post(
        "https://api.openai.com/v1/chat/completions",
        headers=headers,
        json=payload
    )
    
    if not response.ok:
        print(f"Error response: {response.text}")
        raise ValueError(f"API request failed: {response.text}")
        
    result = response.json()
    return (
        result["choices"][0]["message"]["content"],
        result.get("usage", {"prompt_tokens": 0, "completion_tokens": 0, "total_tokens": 0})
    )

def test_hoon_code(input_str: str, hoon_code: str, expected: str) -> Tuple[bool, str, Optional[str]]:
    """Test Hoon code with given input and expected output."""
    combined_input = f"%.  [{input_str}]\n{hoon_code}"
    
    try:
        process = subprocess.Popen(
            ["./urbit", "eval"],
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )
        
        stdout, stderr = process.communicate(input=combined_input)
        
        if process.returncode != 0:
            print(f"Error running `urbit eval`: {stderr}")
            return False, stdout, "command_error"
            
        # Remove ANSI color codes
        actual = re.sub(r'\x1b\[.*?m', '', stdout.strip())
        
        if actual.startswith("/eval"):
            return False, actual, "syntax_error"
            
        for error in ["-find.", "nest-fail", "mint-vain", "mint-loss", "fire-type"]:
            if error in actual:
                return False, actual, "compile_error"
                
        return actual == expected, actual, None
        
    except Exception as e:
        print(f"An error occurred: {e}")
        return False, "", f"command_error: {str(e)}"

def strip_code_fence(response: str) -> str:
    """Remove code fences from the response if present."""
    lines = response.splitlines()
    
    if len(lines) <= 2:
        return response
        
    start = 1 if lines[0].strip().startswith("```") else 0
    end = -1 if lines[-1].strip().startswith("```") else len(lines)
    
    return "\n".join(lines[start:end])

def run_test_case(question_number: int, test_suite: str = "standard") -> Optional[Tuple[str, TestResults, Dict[str, int]]]:
    """Run tests for a single question.
    
    Args:
        question_number: The question number to test
        test_suite: The test suite to use ("standard" or "ez")
    """
    try:
        suite_dir = "questions-ez" if test_suite == "ez" else "questions"
        test_file = read_test_file(f"./{suite_dir}/{question_number}.json")
        with open("system-prompt-small.txt", 'r') as f:
            system_prompt = f.read()
            
        print(f"system prompt length: {len(system_prompt)}")
        print(f"querying ai model for question {question_number}")
        
        response, usage = query_ai_model(system_prompt, test_file.question)
        hoon_code = strip_code_fence(response)
        
        print(f"hoon code: {hoon_code}")
        
        results = []
        for test in test_file.tests:
            passed, actual, error = test_hoon_code(test.input, hoon_code, test.expected)
            results.append(TestResult(test.input, passed, actual, error))
            
        return str(question_number), TestResults(hoon_code, results), usage
        
    except Exception as e:
        print(f"Error processing question {question_number}: {e}")
        return None

def create_run(prompt_text: str, test_suite: str = "standard") -> int:
    """Create a new run record with proper error handling."""
    conn = get_db()
    c = conn.cursor()
    
    try:
        c.execute('BEGIN TRANSACTION')
        
        # Create run record
        c.execute('''
            INSERT INTO runs (model, prompt_strategy, prompt_text, prompt_tokens, timestamp, test_suite)
            VALUES (?, ?, ?, ?, CURRENT_TIMESTAMP, ?)
        ''', ('gpt-4-turbo', 'small_prompt', prompt_text, 0, test_suite))
        
        # Add strategy if it doesn't exist
        c.execute('''
            INSERT OR IGNORE INTO prompt_strategies (name, description)
            VALUES (?, ?)
        ''', ('small_prompt', 'Minimal system prompt with just core instructions'))
        
        run_id = c.lastrowid
        if not run_id:
            raise ValueError("Failed to create run record")
            
        c.execute('COMMIT')
        return run_id
        
    except Exception as e:
        c.execute('ROLLBACK')
        raise e
    finally:
        conn.close()

def save_results(run_id: int, results: Dict[str, Any], token_usage: Dict[str, int]) -> None:
    """Save test results with proper error handling."""
    conn = get_db()
    c = conn.cursor()
    
    try:
        c.execute('BEGIN TRANSACTION')
        
        # Save test results
        for question_num, test_results in results.items():
            for i, test_result in enumerate(test_results['results'], 1):
                c.execute('''
                    INSERT INTO results 
                    (run_id, question_number, test_number, hoon_code, passed, 
                     error_type, error_message, duration_ms)
                    VALUES (?, ?, ?, ?, ?, ?, ?, ?)
                    ON CONFLICT(run_id, question_number, test_number) DO UPDATE SET
                    hoon_code=excluded.hoon_code,
                    passed=excluded.passed,
                    error_type=excluded.error_type,
                    error_message=excluded.error_message,
                    duration_ms=excluded.duration_ms
                ''', (
                    run_id, 
                    int(question_num), 
                    i, 
                    test_results['hoon_code'],
                    test_result['passed'],
                    test_result.get('error'),
                    test_result.get('output'),
                    0  # duration not tracked per test currently
                ))
        
        # Update run with token usage
        total_tokens = token_usage.get('prompt_tokens', 0) + token_usage.get('completion_tokens', 0)
        total_cost = total_tokens * COST_PER_1K_TOKENS / 1000
        
        c.execute('''
            UPDATE runs 
            SET prompt_tokens = ?,
                total_cost = ?
            WHERE id = ?
        ''', (total_tokens, total_cost, run_id))
        
        c.execute('COMMIT')
        
    except Exception as e:
        c.execute('ROLLBACK')
        raise e
    finally:
        conn.close()

def print_summary(run_id: int) -> None:
    """Print test results summary."""
    conn = get_db()
    c = conn.cursor()
    
    try:
        print("\nTest Results Summary:\n")
        
        c.execute('''
            SELECT question_number, COUNT(*) as total_tests,
                   SUM(CASE WHEN passed THEN 1 ELSE 0 END) as passed_tests
            FROM results
            WHERE run_id = ?
            GROUP BY question_number
            ORDER BY question_number
        ''', (run_id,))
        
        for q_num, total_tests, passed_tests in c.fetchall():
            print(f"\nQuestion {q_num} ({passed_tests}/{total_tests} passed):")
            
            c.execute('''
                SELECT test_number, passed, error_type
                FROM results
                WHERE run_id = ? AND question_number = ?
                ORDER BY test_number
            ''', (run_id, q_num))
            
            for test_num, passed, error_type in c.fetchall():
                status = "PASS" if passed else f"FAIL - {error_type}"
                print(f"  Test {test_num}: {status}")
        
        c.execute('''
            SELECT prompt_tokens, total_cost
            FROM runs
            WHERE id = ?
        ''', (run_id,))
        
        tokens, cost = c.fetchone()
        print(f"\nToken Usage Summary:")
        print(f"Total tokens: {tokens:,}")
        print(f"Total cost: ${cost:.2f}")
        
    finally:
        conn.close()

def main(test_suite: str = "standard"):
    """Main program entry point."""
    try:
        # Verify database is intact
        verify_database()
        
        # Read prompt
        with open("system-prompt-small.txt", 'r') as f:
            prompt_text = f.read()
        
        # Create run record
        run_id = create_run(prompt_text, test_suite)
        
        # Get test files
        questions = []
        suite_dir = "questions-ez" if test_suite == "ez" else "questions"
        for entry in os.scandir(f"./{suite_dir}"):
            if entry.name.endswith('.json'):
                if question_number := re.match(r'(\d+)\.json', entry.name):
                    questions.append(int(question_number.group(1)))
        
        # Run tests
        all_results = {}
        total_token_usage = {
            'prompt_tokens': 0,
            'completion_tokens': 0
        }
        
        for question_number in sorted(questions):
            result = run_test_case(question_number, test_suite)
            if result:
                k, v, usage = result
                all_results[k] = {
                    'hoon_code': v.hoon_code,
                    'results': [{'input': r.input, 'passed': r.passed, 'output': r.output, 'error': r.error} 
                              for r in v.results]
                }
                total_token_usage['prompt_tokens'] += usage.get('prompt_tokens', 0)
                total_token_usage['completion_tokens'] += usage.get('completion_tokens', 0)
        
        # Save results
        save_results(run_id, all_results, total_token_usage)
        
        # Print summary
        print_summary(run_id)
        
    except Exception as e:
        print(f"Fatal error: {e}")
        raise

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description='Run HoonGPT tests')
    parser.add_argument('--suite', choices=['standard', 'ez'], default='standard',
                      help='Test suite to run (standard or ez)')
    args = parser.parse_args()
    main(args.suite)