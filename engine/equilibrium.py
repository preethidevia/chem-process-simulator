import numpy as np

def equilibrium_constant(delta_h_kj, T, R=8.314):
    delta_h = delta_h_kj * 1000
    K = np.exp(-delta_h / (R*T))
    return K

def percent_conversion(K):
    return K / (1 + K) * 100
