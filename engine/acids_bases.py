def calculate_pH(addition):
    # simple example
    return 7 - addition

def titration_curve():
    x = [i/100 for i in range(-50,51)]
    y = [calculate_pH(val) for val in x]
    return x, y
