# Sunko-Interpreter

## Table of Contents
1. [Introduction](#introduction)
2. [Installation](#installation)
3. [Getting Started](#getting-started)
    - [Hello World Example](#hello-world-example)
4. [Language Syntax](#language-syntax)
    - [Comments](#comments)
    - [Variables and Data Types](#variables-and-data-types)
    - [Arithmetic Operations](#arithmetic-operations)
    - [Control Flow](#control-flow)
    - [Functions](#functions)
    - [Input and Output](#input-and-output)
    - [Type Casting](#type-casting)
5. [Instruction Set](#instruction-set)
    - [Arithmetic Instructions](#arithmetic-instructions)
    - [Memory Instructions](#memory-instructions)
    - [Control Flow Instructions](#control-flow-instructions)
    - [Input/Output Instructions](#inputoutput-instructions)
    - [Type Casting Instructions](#type-casting-instructions)
    - [Miscellaneous Instructions](#miscellaneous-instructions)
6. [Examples](#examples)
7. [Contributing](#contributing)
8. [License](#license)

# Introduction

Welcome to the documentation for **Sunko**, an assembly-like programming language designed for educational purposes and to provide a clear understanding of low-level programming concepts. Sunko aims to bridge the gap between high-level programming abstractions and the underlying machine operations, offering users a unique platform to explore the fundamentals of computer science, arithmetic operations, memory management, and control flow mechanisms.

Sunko is developed with simplicity, readability, and ease of learning in mind, making it an ideal choice for those new to programming or seeking to deepen their understanding of how software closely interacts with hardware. Despite its simplicity, Sunko is a powerful tool that allows for the development of complex programs and algorithms, from basic arithmetic calculations to advanced control structures.

## Key Features

- **Simplicity**: Sunko's syntax is designed to be straightforward and easy to learn, removing any barriers to entry for beginners.
- **Direct Memory Access**: Directly manipulate recreated memory addresses and registers, offering a hands-on experience with low-level programming.
- **Rich Instruction Set**: A comprehensive set of instructions, including arithmetic operations, control flow, input/output handling, and more.
- **Extensibility**: Easily extend the language with additional instructions and features as needed.
- **Interactive Execution**: Execute Sunko programs interactively, allowing for immediate feedback and experimentation.

Whether you're a student, educator, or hobbyist, Sunko provides a solid foundation for exploring the intricacies of programming languages and understanding the core principles that underpin all software development. Dive into Sunko, and start your journey through the fascinating world of programming at the metal level.




## Installation

Installing Sunko is straightforward. The language is designed to run on multiple platforms, including Windows, macOS, and Linux. Follow these steps to get Sunko up and running on your system:

### Prerequisites

Before installing Sunko, ensure you have the following prerequisites installed on your system:
- Python 3.6 or higher
- Git (optional, for cloning the repository)

### Steps

1. **Clone the Repository** (optional if you're installing from source):
   ```bash
   git clone https://github.com/AntoineBlondon/Sunko-Interpreter.git
   cd Sunko-Interpreter
   ```

## Getting Started

To get started with Sunko, let's write a simple "Hello, World!" program. This example will demonstrate how to output text to the console, introducing you to the basics of Sunko programming.

### Hello World Example

Create a new file named `hello.sko` and open it in your favorite text editor. Enter the following Sunko code:

```
# Hello World in Sunko
PRINT "Hello, World!"
HALT
```

To run the program, use the Sunko interpreter from the command line:

```bash
python3 run.py hello.sko
```

You should see "Hello, World!" printed to the console. Congratulations, you've just written and executed your first Sunko program!

## Language Syntax

Sunko's syntax is designed to be clear and accessible, drawing inspiration from traditional assembly languages while providing modern conveniences. Here's an overview of the key aspects of Sunko's syntax:

### Comments

Comments in Sunko begin with a semicolon (`#`) and extend to the end of the line. Comments are ignored by the interpreter and are useful for adding notes and explanations within your code.

```
# This is a comment
```

### Variables and Data Types

In Sunko, variables are directly associated with registers or memory addresses. The language supports a simple set of data types, primarily integers and strings for simplicity.

```
# Assigning an integer value to a register
SET @0, 10

# Assigning a string value to a register
SET @1, "Hello, Sunko!"
```

### Arithmetic Operations

Sunko supports basic arithmetic operations such as addition, subtraction, multiplication, and division. These operations are performed using specific instructions and can involve immediate values or values stored in registers.

```
# Adding two numbers
SET @0, 5
SET @1, 10
ADD @2, @0, @1  # @2 now contains 15

# Subtracting two numbers
SUB @3, @1, @0  # @3 now contains 5
```

### Control Flow

Control flow in Sunko is managed through conditional execution and function calls. While traditional `JMP` (jump) instructions are not used, conditional calls like `CEQ` (Call if Equal) allow for implementing decision-making logic.

```
# Conditional execution example
SET @0, 10
SET @1, 10
CEQ equal_function, @0, @1  # Calls 'equal_function' if @0 and @1 are equal
```

### Functions

Functions in Sunko allow grouping instructions into reusable blocks. Functions are defined with a name, and they can be called using the `CALL` instruction. 

```
# Function definition
FUNC add_numbers {
    SET @0, 5
    SET @1, 10
    ADD @2, @0, @1
    PRINT @2
}

# Calling a function
CALL add_numbers
```

### Input and Output

Input and output operations are essential for interacting with the user. Sunko provides `INPUT` for reading input from the user and `PRINT` for displaying messages.

```
# Reading input
INPUT @0, "Enter a number: "

# Printing output
PRINT "You entered: "
PRINT @0
```

### Type Casting

In order to insure a smooth execution, one can cast a value to a type. Sunko provides the instructions `INT` and `STR` to transition between the two types.

```
# Casting to integer
INT @0, "3"

# Casting to string
STR @2, 15
```

## Instruction Set

Sunko offers a rich set of instructions designed for direct manipulation of registers and memory, control flow, and interaction with the user. Below is a detailed overview of each instruction available in Sunko.

### Arithmetic Instructions

- **`SET`**: Assigns a value to a register.
  - **Syntax**: `SET register, value`
  - **Example**: `SET @0, 5` assigns the value 5 to register 0.

- **`SWAP`**: Exchanges the values between two registers.
  - **Syntax**: `SWAP register1, register2`
  - **Example**: `SWAP @0, @1` swaps the values of register 0 and register 1.

- **`ADD`**: Adds two values and stores the result in a register.
  - **Syntax**: `ADD register, value1, value2`
  - **Example**: `ADD @2, @0, @1` adds the values of register 0 and register 1, storing the result in register 2.

- **`SUB`**: Subtracts one value from another and stores the result in a register.
  - **Syntax**: `SUB register, value1, value2`
  - **Example**: `SUB @2, @0, @1` subtracts the value of register 1 from register 0, storing the result in register 2.

- **`MUL`**: Multiplies two values and stores the result in a register.
  - **Syntax**: `MUL register, value1, value2`
  - **Example**: `MUL @2, @0, @1` multiplies the values of register 0 and register 1, storing the result in register 2.

- **`DIV`**: Performs integer division of two values and stores the quotient in a register.
  - **Syntax**: `DIV register, value1, value2`
  - **Example**: `DIV @2, @0, @1` divides the value of register 0 by register 1, storing the quotient in register 2.

- **`TDIV`**: Performs true division of two values and stores the result in a register.
  - **Syntax**: `TDIV register, value1, value2`
  - **Example**: `TDIV @2, @0, @1` divides the value of register 0 by register 1, storing the floating-point result in register 2.

- **`MOD`**: Calculates the remainder of division of two values and stores it in a register.
  - **Syntax**: `MOD register, value1, value2`
  - **Example**: `MOD @2, @0, @1` calculates the remainder of dividing the value of register 0 by register 1, storing it in register 2.

### Control Flow Instructions

- **`CALL`**: Calls a function by name.
  - **Syntax**: `CALL function_name`
  - **Example**: `CALL myFunction` calls the function named "myFunction".

- **`CEQ`**: Calls a function if two values are equal.
  - **Syntax**: `CEQ function_name, value1, value2`
  - **Example**: `CEQ equalFunc, @0, @1` calls "equalFunc" if the values of register 0 and register 1 are equal.

- **`CNE`** (Call if Not Equal): Calls a function if two values are not equal.
  - **Syntax**: `CNE function_name, value1, value2`
  - **Example**: `CNE "notEqualFunc", @0, @1` calls "notEqualFunc" if the values in register 0 and register 1 are not equal.

- **`CGT`** (Call if Greater Than): Calls a function if the first value is greater than the second value.
  - **Syntax**: `CGT function_name, value1, value2`
  - **Example**: `CGT "greaterFunc", @0, @1` calls "greaterFunc" if the value in register 0 is greater than the value in register 1.

- **`CLT`** (Call if Less Than): Calls a function if the first value is less than the second value.
  - **Syntax**: `CLT function_name, value1, value2`
  - **Example**: `CLT "lessFunc", @0, @1` calls "lessFunc" if the value in register 0 is less than the value in register 1.

- **`CLE`** (Call if Less Than or Equal): Calls a function if the first value is less than or equal to the second value.
  - **Syntax**: `CLE function_name, value1, value2`
  - **Example**: `CLE "lessEqualFunc", @0, @1` calls "lessEqualFunc" if the value in register 0 is less than or equal to the value in register 1.

- **`CGE`** (Call if Greater Than or Equal): Calls a function if the first value is greater than or equal to the second value.
  - **Syntax**: `CGE function_name, value1, value2`
  - **Example**: `CGE "greaterEqualFunc", @0, @1` calls "greaterEqualFunc" if the value in register 0 is greater than or equal to the value in register 1.

- **`CMP`** (Compare): Compares two values and stores the result in a register. The result is `1` if the values are equal, and `0` otherwise.
  - **Syntax**: `CMP register, value1, value2`
  - **Example**: `CMP @2, @0, @1` compares the values in register 0 and register 1, storing `1` in register 2 if they are equal, or `0` if they are not.


### Input/Output Instructions

- **`INPUT`**: Reads input from the user and stores it in a register.
  - **Syntax**: `INPUT register, "message"`
  - **Example**: `INPUT @0, "Enter a number: "` reads a number from the user and stores it in register 0.

- **`PRINT`**: Prints a value to the console.
  - **Syntax**: `PRINT value`
  - **Example**: `PRINT "Hello, Sunko!"` prints "Hello, Sunko!" to the console.

### Type Casting Instructions

- **`INT`**: Casts a value to an integer and stores it in a register.
  - **Syntax**: `INT register, value`
  - **Example**: `INT @0, "3"` Casts the string "3" to the number 3 and stores it in register 0

- **`STR`**: Casts a value to an string and stores it in a register.
  - **Syntax**: `STR register, value`
  - **Example**: `STR @0, 32` Casts the int 32 to the string "32" and stores it in register 0

### Miscellaneous Instructions

- **`REG`**: Displays the current state of all registers (useful for debugging).
  - **Syntax**: `REG`
  - **Example**: `REG` prints the current state of all registers.

- **`HALT`**: Stops program execution.
  - **Syntax**: `HALT`
  - **Example**: `HALT` stops the program.

This instruction set provides the foundation for programming in Sunko, allowing for a wide range of applications from basic arithmetic to complex control flow and interaction with the user. For detailed usage examples and additional information, refer to the [Examples](#examples) section.


## Examples

Below are some examples to help you get started with Sunko programming:

### Example 1: Adding Two Numbers

This example reads two numbers from the user, adds them, and prints the result.

```
# Read two numbers
INPUT @0, "Enter the first number: "
INPUT @1, "Enter the second number: "

# Add the numbers
ADD @2, @0, @1

# Print the result
PRINT "The sum is: "
PRINT @2
HALT
```

### Example 2: Compare Two Numbers

This example compares two numbers and prints a message based on the comparison.

```
FUNC print_equal {
    PRINT "The numbers are equal."
}

FUNC print_not_equal {
    PRINT "The numbers are not equal."
}

# Assign numbers
SET @0, 10
SET @1, 20

# Compare and call functions based on the result
CMP @2, @0, @1
CEQ print_equal, @2, 1
CEQ print_not_equal, @2, 0
```

### Example 3: Factorial

This example computes the factorial of an input number and prints the result.

```
# Calculates the factorial of the number in @0, result in @RETURN
FUNC Factorial {
    # Initialize the loop counter and the result accumulator
    SET @1, 1  # Loop counter
    SET @2, 1  # Result accumulator

    # Define the loop function for factorial calculation
    FUNC loop {
        MUL @2, @2, @1  # Multiply the accumulator by the loop counter
        ADD @1, @1, 1   # Increment the loop counter
        CLE loop, @1, @0  # If loop counter is less than or equal to @0, continue looping
    }

    # Start the loop if @0 is greater than or equal to 1
    CLE loop, @1, @0

    # Store the final result in @RETURN
    SET @RETURN, @2

    # Reset used registers
    SET @1, 0
    SET @2, 0
}



INPUT @0, "Enter a number: "
INT @0, @0
CALL Factorial
PRINT @RETURN
```


## Contributing

We welcome contributions to Sunko! If you have suggestions for improvements, bug fixes, or new features, please feel free to submit an issue or pull request on our GitHub repository.

## License

Sunko is distributed under the MIT License. See the LICENSE file in our GitHub repository for more details.