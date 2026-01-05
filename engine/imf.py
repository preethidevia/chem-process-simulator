import numpy as np
import pandas as pd
import math

R = 8.314  # J/(mol·K)
A = 1e5    # arbitrary constant for potential energy curve
B = 1e3    # repulsive constant

SUBSTANCES = {
    "H2O": {
        "molar_mass": 18,
        "melting_point": 273,
        "boiling_point": 373,
        "vapor_pressure_298": 3.2,
        "imf": "Hydrogen Bonding",
        "internuclear_distance": 0.096
    },
    "CH4": {
        "molar_mass": 16,
        "melting_point": 91,
        "boiling_point": 112,
        "vapor_pressure_298": 45,
        "imf": "London Dispersion",
        "internuclear_distance": 0.109
    },
    "CO2": {
        "molar_mass": 44,
        "melting_point": 217,
        "boiling_point": 194,
        "vapor_pressure_298": 57,
        "imf": "London Dispersion",
        "internuclear_distance": 0.116
    },
    "NH3": {
        "molar_mass": 17,
        "melting_point": 195,
        "boiling_point": 240,
        "vapor_pressure_298": 8.5,
        "imf": "Hydrogen Bonding",
        "internuclear_distance": 0.101
    }
}

def potential_energy_curve(r_values):
    return (A / r_values**12) - (B / r_values**6)

def generate_potential_energy_data():
    r = np.linspace(0.05, 0.5, 200)
    pe = potential_energy_curve(r)

    return pd.DataFrame({
        "Internuclear Distance (nm)": r,
        "Potential Energy": pe
    })

def generate_bp_mp_vs_molar_mass():
    rows = []

    for name, data in SUBSTANCES.items():
        rows.append({
            "Substance": name,
            "Molar Mass (g/mol)": data["molar_mass"],
            "Boiling Point (K)": data["boiling_point"],
            "Melting Point (K)": data["melting_point"]
        })

    return pd.DataFrame(rows)

def vapor_pressure_curve(vp_298, temperature_range):
    return vp_298 * np.exp(0.05 * (temperature_range - 298))

def generate_vapor_pressure_data(substance, T_min=250, T_max=400):
    T = np.linspace(T_min, T_max, 50)
    vp = vapor_pressure_curve(
        SUBSTANCES[substance]["vapor_pressure_298"],
        T
    )

    return pd.DataFrame({
        "Temperature (K)": T,
        "Vapor Pressure (kPa)": vp
    })

def get_substance_outputs(substance):
    return SUBSTANCES[substance]
