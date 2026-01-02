#Implement:
#pH calculation
#Buffer capacity
#Stability limits
#Outputs:
#pH vs added acid/base
#Safe operating window
#AP Chem: Acids & bases
#ChemE: Process control

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

def calculate_pH(H_concentration):
    """
    Calculates pH from hydrogen ion concentration.
    """
    return -np.log10(H_concentration)

def buffer_safe(pH, min_pH=6.5, max_pH=8.5):
    """
    Checks if pH is within a safe buffer range.
    """
    return min_pH <= pH <= max_pH

def optimize_pH(H_min=1e-8, H_max=1e-6, steps=50):
    """
    Finds an H+ concentration that produces a safe buffer pH.
    """
    H_values = np.linspace(H_min, H_max, steps)
    for H in H_values:
        pH = calculate_pH(H)
        if buffer_safe(pH):
            return H, pH

    # fallback if none found
    H = H_values[0]
    return H, calculate_pH(H)