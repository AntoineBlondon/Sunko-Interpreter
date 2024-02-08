

class AstNode:
    def __init__(self, lineno=None, col_offset=None):
        self.lineno = lineno
        self.col_offset = col_offset

class StatementList(AstNode):
    def __init__(self, statements, lineno=None, col_offset=None):
        super().__init__(lineno, col_offset)
        self.statements = statements
    
    def __str__(self):
        return "\n".join(str(statement) for statement in self.statements)
    


class FunctionDeclaration(AstNode):
    def __init__(self, name, statements, lineno=None, col_offset=None):
        super().__init__(lineno, col_offset)
        self.name = name
        self.statements = statements
    
    def __str__(self):
        return f"FunctionDeclaration(name={self.name}, statements={self.statements})"


class Instruction(AstNode):
    def __init__(self, instruction_name, arguments, lineno=None, col_offset=None):
        super().__init__(lineno, col_offset)
        self.instruction_name = instruction_name
        self.arguments = arguments
    
    def __str__(self):
        return f"Instruction(instruction_name={self.instruction_name}, arguments={self.arguments})"

class ArgumentList(AstNode):
    def __init__(self, arguments, lineno=None, col_offset=None):
        super().__init__(lineno, col_offset)
        self.arguments = arguments
    
    def __str__(self):
        return f"ArgumentList(arguments={[str(x)+', ' for x in self.arguments]})"


class Number(AstNode):
    def __init__(self, value, lineno=None, col_offset=None):
        super().__init__(lineno, col_offset)
        self.value = value
    
    def __str__(self):
        return f"Number(value={self.value})"


class String(AstNode):
    def __init__(self, value, lineno=None, col_offset=None):
        super().__init__(lineno, col_offset)
        self.value = value

    def __str__(self):
        return f"String(value={self.value})"


class Character(AstNode):
    def __init__(self, value, lineno=None, col_offset=None):
        super().__init__(lineno, col_offset)
        self.value = value 
    
    def __str__(self):
        return f"Character(value={self.value})"



class List(AstNode):
    def __init__(self, elements, lineno=None, col_offset=None):
        super().__init__(lineno, col_offset)
        self.elements = elements
    
    def __str__(self):
        return f"List(elements={self.elements})"


class Identifier(AstNode):
    def __init__(self, name, lineno=None, col_offset=None):
        super().__init__(lineno, col_offset)
        self.name = name
    
    def __str__(self):
        return f"Identifier(name={self.name})"


class Register(AstNode):
    def __init__(self, index, lineno=None, col_offset=None):
        super().__init__(lineno, col_offset)
        self.index = index
    
    def __str__(self):
        return f"Register(index={self.index})"