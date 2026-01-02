#Implement:
#ΔG = ΔH − TΔS
#Spontaneity check
#Energy efficiency metric
#Outputs:
#Energy required
#Feasible temperature range
#AP Chem: Thermodynamics
#ChemE: Energy balance

def gibbs_energy(delta_h, delta_s, T):
    delta_g = delta_h - (T * delta_s / 1000)
    spontaneous = delta_g < 0
    return delta_g, spontaneous
