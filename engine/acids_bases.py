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

def calculate_pH(delta_moles, initial_pH=7):
    H = 10 ** (-initial_pH)
    H += delta_moles
    H = max(H, 1e-14)
    return -np.log10(H)

def titration_curve():
    added = np.linspace(-0.5, 0.5, 200)
    pH = [-np.log10(max(10**-7 + x, 1e-14)) for x in added]
    return added, pH
