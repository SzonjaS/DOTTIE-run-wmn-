def AND(inputs):
    return int(all(inputs))

def OR(inputs):
    return int(any(inputs))

def NOT(input_signal):
    return int(not input_signal)

def NAND(inputs):
    return int(NOT(AND(inputs)))
