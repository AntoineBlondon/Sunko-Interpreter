from ply import lex


tokens = (
    'FUNC',
    'IDENTIFIER',
    'REGISTER',
    'NUMBER',
    'LBRACE',
    'RBRACE',
    'COMMA',
    'STRING_LITERAL',
    'CHAR_LITERAL',
    'LBRACKET',
    'RBRACKET',
    'NEWLINE',
)
reserved = {
    'FUNC': 'FUNC',
}

t_LBRACE = r'\{'
t_RBRACE = r'\}'
t_COMMA = r','


t_LBRACKET = r'\['
t_RBRACKET = r'\]'


t_ignore = ' \t'

# Single-line Comment Rule
def t_COMMENT(t):
    r'\#.*'
    pass

# String literal
def t_STRING_LITERAL(t):
    r'"([^"\\]|\\.)*"'
    t.value = t.value[1:-1]  # Remove the quotes
    return t

# Character literal (assuming single quotes for characters)
def t_CHAR_LITERAL(t):
    r"'([^'\\]|\\.)'"
    t.value = t.value[1:-1]  # Remove the quotes
    return t


# Regular expression rules with some action code
def t_REGISTER(t):
    r'@\w+'
    return t

def t_NUMBER(t):
    r'\b\d+(\.\d+)?\b'
    t.value = float(t.value) if '.' in t.value else int(t.value)
    return t

def t_IDENTIFIER(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    t.type = reserved.get(t.value.upper(), 'IDENTIFIER')
    return t

# Rule to track line numbers
def t_NEWLINE(t):
    r'\n+'
    t.lexer.lineno += len(t.value)
    return t

# Error handling rule
def t_error(t):
    print(f"Illegal character '{t.value[0]}' at line {t.lineno}")
    t.lexer.skip(1)

# Build the lexer
lexer = lex.lex()
