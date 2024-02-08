

def is_register(value):
    return type(value) == dict and "index" in value and "value" in value


def get_value(value):
    if is_register(value):
        return value["value"]
    else:
        return value

def get_values(values):
    return [get_value(value) for value in values]