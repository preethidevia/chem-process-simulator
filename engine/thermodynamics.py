def gibbs_energy(delta_h_kj, delta_s_j, T):
    delta_h = delta_h_kj * 1000  # kJ → J
    delta_g = delta_h - T*delta_s_j
    spontaneous = delta_g < 0
    return delta_g/1000, spontaneous  # return kJ
