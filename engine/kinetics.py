#Implement:
#First-order and second-order rate laws
#Arrhenius equation
#Outputs:
#Reaction rate
#Concentration vs time
#AP Chem: Kinetics
#ChemE: Reactor behavior

import numpy as np

R = 8.314  # J/mol·K

# -----------------------------------
# Compound database (simplified)
# -----------------------------------
COMPOUNDS = {
    "Generic A": {"A": 1e7, "Ea": 50000},
    "Hydrogen Peroxide": {"A": 2e8, "Ea": 75000},
    "Nitrogen Dioxide": {"A": 5e6, "Ea": 42000}
}

def arrhenius_rate(T, compound):
    params = COMPOUNDS[compound]
    A = params["A"]
    Ea = params["Ea"]
    return A * np.exp(-Ea / (R * T))

# -----------------------------------
# Zeroth Order
# [A] = [A0] − kt
# -----------------------------------
def zeroth_order_concentration(A0, T, t, compound):
    k = arrhenius_rate(T, compound)
    conc = A0 - k * t
    return np.maximum(conc, 0)

def zeroth_order_half_life(A0, k):
    return A0 / (2 * k)

# -----------------------------------
# First Order
# ln[A] = −kt + ln[A0]
# -----------------------------------
def first_order_concentration(A0, T, t, compound):
    k = arrhenius_rate(T, compound)
    return A0 * np.exp(-k * t)

def first_order_half_life(k):
    return np.log(2) / k

# -----------------------------------
# Second Order
# 1/[A] = kt + 1/[A0]
# -----------------------------------
def second_order_concentration(A0, T, t, compound):
    k = arrhenius_rate(T, compound)
    return 1 / (k * t + (1 / A0))

def second_order_half_life(A0, k):
    return 1 / (k * A0)
