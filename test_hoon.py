import subprocess
import argparse
import re
import sys
import os

def test_hoon_code(hoon_code: str, input_str: str, expected: str) -> bool:
    """
    Test a Hoon function by running it with `urbit eval`.

    Args:
        hoon_code (str): The Hoon code containing the function.
        input_str (str): The input to provide to the Hoon function.
        expected (str): The expected output from the Hoon function.

    Returns:
        bool: True if the output matches the expected output, False otherwise.
    """
    try:
        # Concatenate the Hoon code and input string with a newline
        # Format the Hoon function call in tall form
        # Wrap input in brackets if not empty
        formatted_input = f"[{input_str}]" if input_str else ""
        if input_str:
            combined_input = f"%.\n{formatted_input}\n{hoon_code}"
        else:
            combined_input = hoon_code

        print("Running Hoon code:\n", combined_input)

        # Construct the `urbit eval` command using relative path
        command = ["./urbit", "eval"]

        # Run the command and capture the output
        result = subprocess.run(command, input=combined_input, capture_output=True, text=True)

        # Check if the command succeeded
        if result.returncode != 0:
            print("Error running `urbit eval`:", result.stderr)
            return False

        # Get the actual output
        ansi_escape = re.compile(r'\x1b\[.*?m')
        actual = ansi_escape.sub('', result.stdout.strip())

        print('actual', actual, type(actual), len(actual), repr(actual))
        print('expected', expected, type(expected), len(expected), repr(expected))

        # Compare the actual output to the expected output
        return actual == expected

    except Exception as e:
        print(f"An error occurred: {e}")
        return False

def run_filesystem_tests(test_dir: str):
    """
    Run tests from a directory structure of .in and .out files.
    
    Directory structure expected:
    test_dir/
        problem_name/
            1.in
            1.out
            2.in
            2.out
            ...
    """
    problems = {}
    for root, dirs, files in os.walk(test_dir):
        if not files:
            continue
            
        problem = os.path.relpath(root, test_dir)
        if problem not in problems:
            problems[problem] = {"inputs": [], "outputs": []}
            
        for f in sorted(files):
            if f.endswith('.in'):
                problems[problem]["inputs"].append(os.path.join(root, f))
            elif f.endswith('.out'):
                problems[problem]["outputs"].append(os.path.join(root, f))
                
    total_tests = 0
    failed_tests = []
    
    for problem, tests in problems.items():
        print(f"\nRunning tests for problem: {problem}")
        inputs = sorted(tests["inputs"])
        outputs = sorted(tests["outputs"])
        
        if len(inputs) != len(outputs):
            print(f"Warning: Mismatched number of input/output files for {problem}")
            continue
            
        for input_file, output_file in zip(inputs, outputs):
            test_num = os.path.splitext(os.path.basename(input_file))[0]
            print(f"\nTest {test_num}:")
            
            with open(input_file, 'r') as f:
                input_data = f.read().strip()
            with open(output_file, 'r') as f:
                expected = f.read().strip()
                
            # TODO: Extract hoon_code based on problem name/configuration
            hoon_code = "add"  # Placeholder
            
            result = test_hoon_code(hoon_code, input_data, expected)
            if not result:
                failed_tests.append((problem, test_num))
            total_tests += 1
            print("Pass" if result else "Fail")
    
    print(f"\nTest Summary:")
    print(f"Ran {total_tests} tests across {len(problems)} problems")
    if failed_tests:
        print(f"Failed {len(failed_tests)} tests:")
        for problem, test_num in failed_tests:
            print(f"  Problem {problem}, Test {test_num}")
    else:
        print("All tests passed!")
    
    return len(failed_tests)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Test a Hoon function using `urbit eval`.")
    
    # Add subparsers for different modes
    subparsers = parser.add_subparsers(dest='mode', help='Mode of operation')
    
    # Filesystem test mode
    fs_parser = subparsers.add_parser('fs', help='Run tests from filesystem')
    fs_parser.add_argument('test_dir', type=str, help='Directory containing test files')
    
    # Direct test mode
    direct_parser = subparsers.add_parser('direct', help='Run a single test directly')
    direct_parser.add_argument("hoon_code", type=str, help="The Hoon code containing the function.")
    direct_parser.add_argument("input_str", type=str, help="The input to provide to the Hoon function.")
    direct_parser.add_argument("expected_output", type=str, help="The expected output from the Hoon function.")
    
    # Built-in test suite mode
    test_parser = subparsers.add_parser('test', help='Run built-in test suite')

    args = parser.parse_args()
    
    if args.mode == 'fs':
        # Run tests from filesystem
        exit_code = run_filesystem_tests(args.test_dir)
        sys.exit(exit_code)
        
    elif args.mode == 'direct':
        # Run a single direct test
        result = test_hoon_code(args.hoon_code, args.input_str, args.expected_output)
        print(result)
        print("Pass" if result else "Fail")
        sys.exit(0 if result else 1)
        
    elif args.mode == 'test':
        # Run built-in test suite
        test_cases = [
            # (hoon_code, input_str, expected_output)
            ("add", "5 5", "10"),
            ("mul", "6 7", "42"),
            ("sub", "20 8", "12"),
            ("div", "10 2", "5"),
            # Identity function test
            ("|=  a=*  a", "42", "42"),
        ]
        
        failed_tests = []
        for i, (code, input_str, expected) in enumerate(test_cases, 1):
            print(f"\nRunning test {i}: {code} with input {input_str}")
            result = test_hoon_code(code, input_str, expected)
            if not result:
                failed_tests.append((i, code, input_str, expected))
            print("Pass" if result else "Fail")
        
        print("\nTest Summary:")
        print(f"Ran {len(test_cases)} tests")
        if failed_tests:
            print(f"Failed {len(failed_tests)} tests:")
            for test_num, code, input_str, expected in failed_tests:
                print(f"  Test {test_num}: {code} with input {input_str} (expected {expected})")
        else:
            print("All tests passed!")
        
        sys.exit(len(failed_tests))
    
    else:
        parser.print_help()
        sys.exit(1)
