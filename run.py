import sys
from sunko_parser import parser  # Import the parser you've created
from sunko_runtime import Runtime
import re

def preprocess_source_code(source_code):
    # Replace comments with a newline to preserve line numbers
    processed_code = re.sub(r'\#.*\n', '\n', source_code)
    return processed_code.strip() + '\n'


def run_script(filename):
    # Read the source file
    with open(filename, 'r') as file:
        source_code = file.read()

    # Parse the source code into an AST
    ast = parser.parse(preprocess_source_code(source_code))

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
