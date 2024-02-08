from sunko_context_manager import ContextManager
import sunko_instructions

class Runtime:
    def __init__(self, debug=False):
        self.context = ContextManager()
        self.context.set_runtime(self)
        self.is_running = True
        self.debug = debug
        self.registers = self.initialize_registers()
        self.functions = {}
        self.memory = {}
    
    def initialize_registers(self):
        r = {x:0 for x in range(32)}
        r["RETURN"] = 0
        return r

    def store_to_register(self, register, value):
        self.registers[register] = value
    
    def load_from_register(self, register):
        return self.registers[register]
    
    def store_to_memory(self, address, value):
        self.memory[address] = value
    
    def load_from_memory(self, address):
        if address not in self.memory:
            return 0
        return self.memory[address]
    


    def evaluate(self, node):
        if self.debug: print(node)
        method_name = 'evaluate_' + type(node).__name__
        method = getattr(self, method_name, self.generic_evaluate)
        return method(node)

    def evaluate_int(self, node):
        return node

    def evaluate_float(self, node):
        return node

    def evaluate_str(self, node):
        return node

    def evaluate_Number(self, node):
        return node.value

    def evaluate_String(self, node):
        return node.value

    def evaluate_List(self, node):
        return [self.evaluate(element) for element in node.elements]
    
    def evaluate_FunctionDeclaration(self, node):
        self.functions[node.name] = node
    

    def evaluate_FunctionCall(self, node):
        if node.name not in self.functions:
            raise Exception(f"Function '{node.name}' not defined.")
        function_node = self.functions[node.name]
        for statement in function_node.statements:
            self.evaluate(statement)
    
    def evaluate_Instruction(self, node):
        
        instruction_func = getattr(sunko_instructions, node.instruction_name.upper(), None)
        
        if instruction_func is None:
            raise NotImplementedError(f"Instruction '{node.instruction_name}' not implemented.")

        # Evaluate arguments
        evaluated_args = self.evaluate(node.arguments)

        # Call the instruction function with the runtime itself and the evaluated arguments
        instruction_func(*evaluated_args)

    
    def evaluate_ArgumentList(self, node):
        return [self.evaluate(arg) for arg in node.arguments]

    def evaluate_StatementList(self, node):
        for statement in node.statements:
            self.evaluate(statement)

    def evaluate_Register(self, node):
        register_index = node.index

        if isinstance(register_index, str):
            if register_index in self.registers:
                return {"index": register_index, "value": self.registers[register_index]}
            else:
                raise IndexError(f"Register '{register_index}' not found.")
        elif isinstance(register_index, int):
            if 0 <= register_index < 32:
                return {"index": register_index, "value": self.registers[register_index]}
            else:
                raise IndexError(f"Register index out of bounds: {register_index}")

    def evaluate_Identifier(self, node):
        return node.name



    def generic_evaluate(self, node):
        raise NotImplementedError(f"Evaluation not implemented for node type: {type(node).__name__}")
