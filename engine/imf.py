def vapor_pressure_curve():
    T = list(range(250,1001,25))
    Pvap = [0.01*(temp-250)**1.5 for temp in T]
    return T, Pvap

def phase_prediction(T, P):
    if T < 300:
        return "Solid"
    elif T < 600:
        return "Liquid"
    else:
        return "Gas"
