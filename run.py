import sys
from sunko_parser import parser  # Import the parser you've created
from sunko_runtime import Runtime

def run_script(filename):
    # Read the source file
    with open(filename, 'r') as file:
        source_code = file.read()

    # Parse the source code into an AST
    ast = parser.parse(source_code)

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
