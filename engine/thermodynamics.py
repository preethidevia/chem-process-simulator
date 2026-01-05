import numpy as np

R = 8.314  # J/mol·K

SPECIES = {
    "None": {"Hf": 0},
    "Hydrogen (H2)": {"Hf": 0},
    "Oxygen (O2)": {"Hf": 0},
    "Water (H2O)": {"Hf": -286000},
    "Carbon Dioxide (CO2)": {"Hf": -394000},
    "Methane (CH4)": {"Hf": -75000},
    "Ammonia (NH3)": {"Hf": -46000},
}
HEAT_CAPACITY = {
    "Water (H2O)": 4.18,
    "Methane (CH4)": 2.22,
    "Ammonia (NH3)": 4.7,
    "Carbon Dioxide (CO2)": 0.84,
}
def reaction_enthalpy(reactants, products):
    """
    ΔH = ΣH(products) − ΣH(reactants)
    """
    H_react = sum(SPECIES[r]["Hf"] for r in reactants if r != "None")
    H_prod = sum(SPECIES[p]["Hf"] for p in products if p != "None")
    return H_prod - H_react

def reaction_profile(delta_h, Ea_forward, has_intermediate=False, catalyst=False):
    """
    Generates energy profile points for reaction coordinate
    """
    x = np.linspace(0, 1, 400)

    # Base energies
    E_reactants = 0
    E_products = delta_h

    Ea = Ea_forward * (0.6 if catalyst else 1.0)

    if has_intermediate:
        E_intermediate = Ea * 0.4
        y = (
            Ea * np.exp(-((x - 0.3) ** 2) / 0.002)
            + E_intermediate * np.exp(-((x - 0.6) ** 2) / 0.002)
        )
    else:
        y = Ea * np.exp(-((x - 0.5) ** 2) / 0.01)

    y = y + (E_products * x)

    return x, y, Ea, np.max(y)

def heat_curve(T_initial, delta_h, steps=200):
    """
    Simulated heating/cooling curve
    """
    heat_added = np.linspace(0, abs(delta_h), steps)

    if delta_h > 0:
        temperature = T_initial + heat_added / 1000
    else:
        temperature = T_initial - heat_added / 1000

    return heat_added, temperature

def substance_heating_curve(substance, T_initial=300, q_max=500):
    heat = np.linspace(0, q_max, 300)

    if substance == "Water (H2O)":
        temp = np.piecewise(
            heat,
            [heat < 100, (heat >= 100) & (heat < 300), heat >= 300],
            [
                lambda q: T_initial + 0.5*q,
                lambda q: T_initial + 50,
                lambda q: T_initial + 50 + 0.3*(q - 300),
            ]
        )
    else:
        Cp = HEAT_CAPACITY.get(substance, 3.0)
        temp = T_initial + heat / Cp

    return heat, temp

def gibbs_energy(delta_h_kj, delta_s_j, T):
    delta_h = delta_h_kj * 1000
    delta_g = delta_h - T*delta_s_j
    spontaneous = delta_g < 0
    return delta_g/1000, spontaneous
