def AND(inputs):
    """Returns 1 if all inputs are 1, otherwise 0"""
    return int(all(inputs))

def OR(inputs):
    """Returns 1 if any input is 1, otherwise 0"""
    return int(any(inputs))

def NOT(input_signal):
    """Returns 1 if input is 0, otherwise 0"""
    return int(not input_signal)

def NAND(inputs):
    """Returns 0 if all inputs are 1, otherwise 1"""
    return int(NOT(AND(inputs)))