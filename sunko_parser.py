from ply import yacc
from sunko_lexer import tokens  # Make sure to replace 'your_lexer_file_name' with the actual name of your lexer file
from sunko_ast_nodes import *


# Program structure
def p_program(p):
    'program : statement_list'
    p[0] = StatementList(p[1], lineno=p.lineno(1))

def p_statement_list(p):
    '''statement_list : statement_list statement
                      | statement'''
    if len(p) == 3:
        p[0] = p[1] + [p[2]]
    else:
        p[0] = [p[1]]

def p_statement(p):
    '''statement : function_definition
                 | expression
                 | instruction_or_function_call'''
    p[0] = p[1]

# Function definition
def p_function_definition(p):
    'function_definition : FUNC IDENTIFIER LBRACE statement_list RBRACE'
    p[0] = FunctionDeclaration(name=p[2], stataments=p[4])


def p_number(p):
    '''expression : NUMBER'''
    p[0] = Number(value=p[1])

def p_string(p):
    '''expression : STRING_LITERAL'''
    p[0] = String(value=p[1])

def p_character(p):
    '''expression : CHAR_LITERAL'''
    p[0] = Character(value=p[1])


# List expressions
def p_list_expression(p):
    'expression : LBRACKET expression_list RBRACKET'
    p[0] = List(elements=p[2])

def p_expression_list(p):
    '''expression_list : expression_list COMMA expression
                       | expression'''
    if len(p) == 4:
        p[0] = p[1] + [p[3]]
    else:
        p[0] = [p[1]]



# Instruction or function call with variable arguments
def p_instruction_or_function_call(p):
    'instruction_or_function_call : IDENTIFIER argument_list_optional'
    p[0] = Instruction(instruction_name=p[1], arguments=p[2])

# Handling an optional argument list for instructions
def p_argument_list_optional(p):
    '''argument_list_optional : argument_list
                              | empty'''
    p[0] = ArgumentList(arguments=p[1]) if p[1] else []

# Handling the argument list for instructions
def p_argument_list(p):
    '''argument_list : argument_list COMMA argument
                     | argument'''
    if len(p) == 4:  # Multiple arguments
        p[0] = p[1] + [p[3]]
    else:  # Single argument
        p[0] = [p[1]]

# Defining what constitutes an argument
def p_argument(p):
    '''argument : IDENTIFIER
                | REGISTER
                | NUMBER
                | STRING_LITERAL
                | CHAR_LITERAL'''
    p[0] = p[1]

# Rule for handling an empty production
def p_empty(p):
    'empty :'
    pass

# Error rule for syntax errors
def p_error(p):
    print("Syntax error in input!")

# Build the parser
parser = yacc.yacc()
