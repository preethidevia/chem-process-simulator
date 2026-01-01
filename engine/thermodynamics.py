#Implement:
#ΔG = ΔH − TΔS
#Spontaneity check
#Energy efficiency metric
#Outputs:
#Energy required
#Feasible temperature range
#AP Chem: Thermodynamics
#ChemE: Energy balance

def gibbs_free_energy(delta_H, delta_S, T):
    """Compute ΔG = ΔH - TΔS"""
    return delta_H - T * delta_S

def energy_cost(delta_H, conversion):
    """Estimate energy cost"""
    return abs(delta_H) * conversion

# ------------------ Optimization for Thermodynamics ------------------
def optimize_energy(delta_H, delta_S):
    """
    Finds temperature with lowest energy cost while maintaining spontaneity (ΔG < 0)
    """
    best_T = 0
    min_energy = float('inf')
    for T in range(300, 900, 10):
        delta_G = gibbs_free_energy(delta_H, delta_S, T)
        if delta_G < 0:
            energy = abs(delta_H)
            if energy < min_energy:
                min_energy = energy
                best_T = T
    return best_T, min_energy
