#Implement:
#pH calculation
#Buffer capacity
#Stability limits
#Outputs:
#pH vs added acid/base
#Safe operating window
#AP Chem: Acids & bases
#ChemE: Process control

import numpy as np
from engine.thermodynamics import gibbs_free_energy

def equilibrium_constant(delta_G, T):
    R = 8.314
    return np.exp(-delta_G / (R * T))

def yield_from_equilibrium(K):
    return K / (1 + K)

def optimize_equilibrium(delta_H, delta_S):
    """
    Finds temperature that maximizes reaction yield
    """
    best_T = 0
    best_yield = 0
    for T in range(300, 900, 10):
        delta_G = gibbs_free_energy(delta_H, delta_S, T)
        K = equilibrium_constant(delta_G, T)
        y = yield_from_equilibrium(K)
        if y > best_yield:
            best_yield = y
            best_T = T
    return best_T, best_yield
