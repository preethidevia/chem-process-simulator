import numpy as np

R = 8.314  # J/mol·K

COMPOUNDS = {
    "Generic A": {"A": 1e7, "Ea": 50000, "order": "variable", "mass": 3.32e-26},
    "Hydrogen Peroxide": {"A": 2e8, "Ea": 75000, "order": "variable", "mass": 4.82e-26},
    "Nitrogen Dioxide": {"A": 5e6, "Ea": 42000, "order": "variable", "mass": 7.65e-26},
    "Oxygen (O2)": {"A": 1e7, "Ea": 40000, "order": "variable", "mass": 5.32e-26},
    "Hydrogen (H2)": {"A": 1.5e7, "Ea": 45000, "order": "variable", "mass": 3.32e-27},
    "Carbon-14 (Nuclear)": {"k": 0.00012, "order": "first", "mass": 2.32e-26, "Ea": 1e-20},
    "Uranium-235 (Nuclear)": {"k": 0.00005, "order": "first", "mass": 3.91e-25, "Ea": 1e-20}
}

def arrhenius_rate(T, compound):
    if "Nuclear" in compound:
        return COMPOUNDS[compound]["k"]
    else:
        params = COMPOUNDS[compound]
        A = params["A"]
        Ea = params["Ea"]
        return A * np.exp(-Ea / (R * T))

def zeroth_order_concentration(A0, T, t, compound):
    k = arrhenius_rate(T, compound)
    conc = A0 - k * t
    return np.maximum(conc, 0)

def zeroth_order_half_life(A0, k):
    return A0 / k

def first_order_concentration(A0, T, t, compound):
    k = arrhenius_rate(T, compound)
    return A0 * np.exp(-k * t)

def first_order_half_life(k):
    return np.log(2) / k

def second_order_concentration(A0, T, t, compound):
    k = arrhenius_rate(T, compound)
    return 1 / (k * t + 1/A0)

def second_order_half_life(A0, k):
    return 1 / (k * A0)

def maxwell_boltzmann_distribution(T, mass, num_points=300):
    kB = 1.380649e-23
    v_max = np.sqrt(10 * kB * T / mass)
    v = np.linspace(0, v_max, num_points)
    KE = 0.5 * mass * v**2
    f_v = 4*np.pi*(mass/(2*np.pi*kB*T))**1.5 * v**2 * np.exp(-mass*v**2/(2*kB*T))
    f_v /= np.max(f_v)
    return KE, f_v
