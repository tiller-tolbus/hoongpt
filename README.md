
The program will:
- Process all JSON files in the `questions` directory
- Generate Hoon code solutions using GPT-4
- Test each solution against the provided test cases
- Save results in the `results` directory with timestamp-based filenames
- Display a summary of test results in the console

## Output

The program generates two types of output:

1. Console output showing:
   - Test progress
   - Summary of passed/failed tests for each question
   - Individual test case results

2. JSON results file in the `results` directory containing:
   - Generated Hoon code
   - Detailed test results
   - Error messages (if any)

## Error Types

The test runner handles several types of errors:
- `syntax_error`: Invalid Hoon syntax
- `compile_error`: Hoon compilation failures
- `command_error`: Issues with the Urbit binary execution
- `unexpected_output`: Output doesn't match expected result

## Environment Variables

The program requires the following environment variable to be set:

`OPENAI_API_KEY` - Your OpenAI API key for accessing GPT-4

You can set this by:
1. Creating a `.env` file in the project root
2. Adding the line: `OPENAI_API_KEY=your_api_key_here`

Or by setting it directly in your shell:
