import sys
from sunko_parser import parser  # Import the parser you've created
from sunko_runtime import Runtime
import re

def preprocess_source_code(source_code):
    # Step 1: Remove comments, replace them with a newline to preserve line numbers
    no_comments_code = re.sub(r'\#.*', '', source_code)
    
    # Step 2: Replace multiple consecutive newlines with a single newline
    # This step is crucial to ensure no more than one newline appears in a row
    condensed_code = re.sub(r'\n\s*\n', '\n', no_comments_code)
    
    # Step 3: Strip leading and trailing whitespace to clean up the code
    # and add a single newline at the end of the code to maintain file structure
    final_code = condensed_code.strip() + '\n'
    
    return final_code

def run_script(filename):
    # Read the source file
    with open(filename, 'r') as file:
        source_code = file.read()

    processed_code = preprocess_source_code(source_code)
    # Parse the source code into an AST
    ast = parser.parse(processed_code)

    # Initialize the runtime environment
    runtime = Runtime(debug=False)

    # Evaluate the AST
    runtime.evaluate(ast)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python run.py <filename>")
        sys.exit(1)
    
    filename = sys.argv[1]
    run_script(filename)
