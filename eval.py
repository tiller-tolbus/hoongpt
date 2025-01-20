import subprocess
import argparse
import re
import sys

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

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Test a Hoon function using `urbit eval`.")
    parser.add_argument("--test", action="store_true", help="Run the test suite")
    parser.add_argument("hoon_code", nargs="?", type=str, help="The Hoon code containing the function.")
    parser.add_argument("input_str", nargs="?", type=str, help="The input to provide to the Hoon function.")
    parser.add_argument("expected_output", nargs="?", type=str, help="The expected output from the Hoon function.")

    args = parser.parse_args()
    
    # Validate arguments
    if not args.test and (args.hoon_code is None or args.input_str is None or args.expected_output is None):
        parser.error("Must provide hoon_code, input_str, and expected_output unless running tests")
        
    print(args)

    # Check if we're running tests
    if args.test:
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
        result = test_hoon_code(args.hoon_code, args.input_str, args.expected_output)
        print(result)
        print("Pass" if result else "Fail")
