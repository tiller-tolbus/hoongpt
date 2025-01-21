use std::fs::File;
use std::io::{Read, Write};
use std::process::{Command, Stdio};
use serde::{Deserialize, Serialize};
use reqwest;
use regex::Regex;
use dotenv::dotenv;
#[derive(Debug, Serialize, Deserialize)]
struct TestCase {
    input: String,
    expected: String,
}

#[derive(Debug, Serialize, Deserialize)]
struct TestFile {
    question: String,
    tests: Vec<TestCase>,
}

fn read_test_file(file_path: &str) -> Result<TestFile, Box<dyn std::error::Error>> {
    // Read file contents
    let mut file = File::open(file_path)?;
    let mut contents = String::new();
    file.read_to_string(&mut contents)?;

    // Parse JSON
    let data: TestFile = serde_json::from_str(&contents)?;

    Ok(data)
}

async fn query_ai_model(system_prompt: &str, user_prompt: &str) -> Result<String, Box<dyn std::error::Error>> {
    let client = reqwest::Client::new();

    let payload = serde_json::json!({
        "model": "gpt-4o",
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
    });
    let auth_token = std::env::var("OPENAI_API_KEY")
        .map_err(|_| "OPENAI_API_KEY environment variable not set")?;

    let response = client.post("https://api.openai.com/v1/chat/completions")
        .header("Authorization", format!("Bearer {}", auth_token))
        .header("Content-Type", "application/json")
        .json(&payload)
        .send()
        .await?;

    let result: serde_json::Value = response.json().await?;

    
    Ok(result["choices"][0]["message"]["content"]
        .as_str()
        .unwrap_or("")
        .to_string())
}
#[derive(Debug)]
enum TestError {
    CommandError(String),
    SyntaxError,
    CompileError,
    UnexpectedOutput(String),
}

fn test_hoon_code(input_str: &str, hoon_code: &str, expected: &str) -> Result<bool, TestError> {
    let combined_input = format!("%.  [{}]\n{}", input_str, hoon_code);

    let mut child = Command::new("urbit")
        .arg("eval")
        .stdin(Stdio::piped())
        .stdout(Stdio::piped())
        .stderr(Stdio::piped())
        .spawn()
        .map_err(|e| TestError::CommandError(e.to_string()))?;

    let mut child_stdin = child.stdin.take().unwrap();
    child_stdin.write_all(combined_input.as_bytes())
        .map_err(|e| TestError::CommandError(e.to_string()))?;
    core::mem::drop(child_stdin);

    match child.wait_with_output() {
        Ok(output) => {
            if !output.status.success() {
                let err = String::from_utf8_lossy(&output.stderr);
                eprintln!("Error running `urbit eval`: {}", err);
                return Ok(false);
            }

            let stdout = String::from_utf8_lossy(&output.stdout);
            let re = Regex::new(r"\x1b\[.*?m").unwrap();
            let actual = re.replace_all(&stdout.trim(), "");

            if actual.starts_with("/eval") {
                return Err(TestError::SyntaxError);
            }
            if actual.contains("-find.") || actual.contains("nest-fail") || 
               actual.contains("mint-vain") || actual.contains("mint-loss") {
                return Err(TestError::CompileError);
            }

            Ok(actual == expected)
        },
        Err(e) => {
            eprintln!("An error occurred: {}", e);
            Err(TestError::CommandError(e.to_string()))
        }
    }
}

fn strip_code_fence(response: &str) -> String {
    let lines: Vec<&str> = response.lines().collect();
    
    if lines.len() <= 2 {
        return response.to_string();
    }

    // Skip first and last line if they contain code fences
    let start = if lines[0].trim().starts_with("```") { 1 } else { 0 };
    let end = if lines[lines.len()-1].trim().starts_with("```") { lines.len()-1 } else { lines.len() };

    lines[start..end].join("\n")
}

#[derive(Debug, Serialize, Deserialize)]
struct TestResult {
    input: String,
    passed: bool,
    error: Option<String>,
}

#[derive(Debug, Serialize, Deserialize)]
struct TestResults {
    hoon_code: String,
    results: Vec<TestResult>,
}

async fn run_test_case(question_number: usize) -> Result<(), Box<dyn std::error::Error>> {
    let test_file = read_test_file(&format!("./questions/{}.json", question_number))?;
    let system_prompt = std::fs::read_to_string("system-prompt.txt")?;
    
    println!("querying ai model for question {}", question_number);
    let response = query_ai_model(
        &system_prompt,
        &test_file.question
    ).await?;
    let hoon_code = strip_code_fence(&response);

    let test_results = TestResults {
        hoon_code: hoon_code.to_string(),
        results: test_file.tests
            .iter()
            .enumerate()
            .map(|(i, test)| {
                println!("Running test for question {} - test index: {}", question_number, i);
                match test_hoon_code(&test.input, &hoon_code, &test.expected) {
                    Ok(passed) => TestResult {
                        input: test.input.clone(),
                        passed,
                        error: None,
                    },
                    Err(TestError::CompileError) => {
                        TestResult {
                            input: test.input.clone(),
                            passed: false,
                            error: Some("compile_error".to_string()),
                        }
                    },
                    Err(TestError::SyntaxError) => {
                        TestResult {
                            input: test.input.clone(),
                            passed: false,
                            error: Some("syntax_error".to_string()),
                        }
                    },
                    Err(TestError::CommandError(e)) => {
                        TestResult {
                            input: test.input.clone(),
                            passed: false,
                            error: Some(format!("command_error: {}", e)),
                        }
                    },
                    Err(TestError::UnexpectedOutput(output)) => {
                        TestResult {
                            input: test.input.clone(),
                            passed: false,
                            error: Some(format!("unexpected_output: {}", output)),
                        }
                    }
                }
            })
            .collect(),
    };
    
    let json = serde_json::to_string_pretty(&test_results)?;
    std::fs::write(&format!("results/{}.json", question_number), json)?;

    Ok(())
}

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    dotenv().ok();
    // Get all question files from the questions directory
    let questions_dir = std::fs::read_dir("./questions")?;
    
    for entry in questions_dir {
        let entry = entry?;
        let path = entry.path();
        
        // Skip non-JSON files
        if path.extension().and_then(|ext| ext.to_str()) != Some("json") {
            continue;
        }
        
        // Extract question number from filename
        if let Some(question_number) = path.file_stem()
            .and_then(|stem| stem.to_str())
            .and_then(|stem| stem.parse::<usize>().ok()) 
        {
            if let Err(e) = run_test_case(question_number).await {
                eprintln!("Error processing question {}: {}", question_number, e);
            }
        }
    }

    println!("\nTest Results Summary: \n");
    let results_dir = std::fs::read_dir("./results")?;
    
    for entry in results_dir {
        let entry = entry?;
        let path = entry.path();
        
        if path.extension().and_then(|ext| ext.to_str()) != Some("json") {
            continue;
        }
        let contents = std::fs::read_to_string(&path)?;
        let results: TestResults = serde_json::from_str(&contents)?;
        if let Some(number) = path.file_stem().and_then(|s| s.to_str()) {
            let total_tests = results.results.len();
            let passed_tests = results.results.iter().filter(|r| r.passed).count();
            println!("\nQuestion {} ({}/{} passed):", number, passed_tests, total_tests);
            
            for (i, test) in results.results.iter().enumerate() {
                let status = if test.passed {
                    "PASS".to_string()
                } else {
                    match &test.error {
                        Some(err) => format!("FAIL - {}", err),
                        None => "FAIL".to_string()
                    }
                };
                println!("  Test {}: {}", i + 1, status);
            }
        }
    }
    Ok(())
}
