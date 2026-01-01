#Implement:
#First-order and second-order rate laws
#Arrhenius equation
#Outputs:
#Reaction rate
#Concentration vs time
#AP Chem: Kinetics
#ChemE: Reactor behavior

import numpy as np

def reaction_rate(T, A=1e7, Ea=80000):
    """
    Calculate reaction rate using Arrhenius equation.
    """
    return A * np.exp(-Ea / (8.314 * T))

def concentration_vs_time(rate, C0=1.0, t_end=50, steps=100):
    """
    Compute concentration over time for first-order reaction
    """
    t = np.linspace(0, t_end, steps)
    C = C0 * np.exp(-rate * t)
    return t, C

# ------------------ Optimization for Kinetics ------------------
def optimize_rate(A=1e7, Ea=80000):
    """
    Finds the temperature that maximizes reaction rate in a practical range
    """
    best_T = 0
    max_rate = 0
    for T in range(300, 900, 10):
        r = reaction_rate(T, A, Ea)
        if r > max_rate:
            max_rate = r
            best_T = T
    return best_T, max_rate
