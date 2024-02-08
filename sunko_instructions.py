from sunko_context_manager import ContextManager
from sunko_register_utils import *

def SET(*args):
    register, value = args
    runtime = ContextManager().get_runtime()
    value = get_value(value)
    runtime.store_to_register(register["index"], value)

def SWAP(*args):
    register1, register2 = args
    runtime = ContextManager().get_runtime()
    value1 = runtime.load_from_register(register1["index"])
    value2 = runtime.load_from_register(register2["index"])
    runtime.store_to_register(register1["index"], value2)
    runtime.store_to_register(register2["index"], value1)

def ADD(*args):
    register, value1, value2 = args
    runtime = ContextManager().get_runtime()
    value1, value2 = get_values([value1, value2])
    runtime.store_to_register(register["index"], value1 + value2)

def SUB(*args):
    register, value1, value2 = args
    runtime = ContextManager().get_runtime()
    value1, value2 = get_values([value1, value2])
    runtime.store_to_register(register["index"], value1 - value2)

def MUL(*args):
    register, value1, value2 = args
    runtime = ContextManager().get_runtime()
    value1, value2 = get_values([value1, value2])
    runtime.store_to_register(register["index"], value1 * value2)

def DIV(*args):
    register, value1, value2 = args
    runtime = ContextManager().get_runtime()
    value1, value2 = get_values([value1, value2])
    runtime.store_to_register(register["index"], value1 // value2)

def MOD(*args):
    register, value1, value2 = args
    runtime = ContextManager().get_runtime()
    value1, value2 = get_values([value1, value2])
    runtime.store_to_register(register["index"], value1 % value2)



def CALL(*args):
    function_name = args[0]

    runtime = ContextManager().get_runtime()
    runtime.store_to_register("RETURN", 0)
    
    body = runtime.functions[function_name].statements
    runtime.evaluate(body)

def CEQ(*args):
    function_name, value1, value2 = args

    runtime = ContextManager().get_runtime()
    value1, value2 = get_values([value1, value2])

    if value1 == value2:
        CALL(function_name)

def INPUT(*args):
    register = args[0]
    message = ""
    if len(args) > 1:
        message = args[1]
    runtime = ContextManager().get_runtime()
    value = input(message)
    runtime.store_to_register(register["index"], value)

def PRINT(*args):
    value = args[0]
    print(get_value(value))

def REG(*args):
    print(args)
    print(ContextManager().get_runtime().registers)


def HALT(*args):
    ContextManager().get_runtime().is_running = False
    pass