from sunko_context_manager import ContextManager
from sunko_register_utils import *

def SET(*args):
    register, value = args
    runtime = ContextManager().get_runtime()
    value = get_value(value)
    runtime.store_to_register(register["index"], value)

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


def CALL(*args):
    function_name = args[0]
    runtime = ContextManager().get_runtime()
    body = runtime.functions[function_name].statements
    runtime.evaluate(body)

def PRINT(*args):
    value = args[0]
    print(get_value(value))

def REG():
    print(ContextManager().get_runtime().registers)