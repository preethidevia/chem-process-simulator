#Implement:
#Equilibrium constant K
#Le Châtelier effects
#Yield vs temperature/pressure
#Outputs:
#% conversion
#Optimal conditions
#AP Chem: Equilibrium
#ChemE: Process optimization

import numpy as np

R = 8.314

def equilibrium_constant(delta_h, T):
    return np.exp(-delta_h * 1000 / (R * T))

def percent_conversion(K):
    return (K / (1 + K)) * 100
