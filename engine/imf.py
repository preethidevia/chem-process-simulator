#Implement:
#Vapor pressure estimation
#Phase prediction
#Solvent effects
#Outputs:
#Phase (gas/liquid)
#Separation feasibility
#AP Chem: IMFs
#ChemE: Materials & separation

import numpy as np

def vapor_pressure_curve():
    T = np.linspace(250, 600, 200)
    P = np.exp(-5000 / T)
    return T, P

def phase_prediction(T, P):
    return "Gas" if T > 373 and P < 5 else "Liquid"
