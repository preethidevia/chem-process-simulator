import math
import pandas as pd

R = 8.314  # J/mol*K

SUBSTANCES = {
    "H2O": {
        "molar_mass": 18.02,
        "polarity": "Polar",
        "imf": "Hydrogen Bonding",
        "bp": 373,
        "mp": 273,
        "en_diff": 1.4
    },
    "NH3": {
        "molar_mass": 17.03,
        "polarity": "Polar",
        "imf": "Hydrogen Bonding",
        "bp": 240,
        "mp": 195,
        "en_diff": 0.9
    },
    "CH4": {
        "molar_mass": 16.04,
        "polarity": "Nonpolar",
        "imf": "London Dispersion Forces",
        "bp": 112,
        "mp": 91,
        "en_diff": 0.4
    },
    "CO2": {
        "molar_mass": 44.01,
        "polarity": "Nonpolar",
        "imf": "London Dispersion Forces",
        "bp": 194,
        "mp": 216,
        "en_diff": 0.9
    },
    "NaCl": {
        "molar_mass": 58.44,
        "polarity": "Ionic",
        "imf": "Ionic Forces",
        "bp": 1738,
        "mp": 1074,
        "en_diff": 2.1
    }
}

PERIODIC_TRENDS = pd.DataFrame({
    "Element": ["Li", "C", "N", "O", "F"],
    "Atomic Number": [3, 6, 7, 8, 9],
    "Atomic Radius (pm)": [152, 77, 75, 73, 71],
    "Electronegativity": [0.98, 2.55, 3.04, 3.44, 3.98],
    "Ionization Energy (kJ/mol)": [520, 1086, 1402, 1314, 1681]
})

def get_substance_data(name):
    if name in SUBSTANCES:
        return SUBSTANCES[name]
    return None

def predict_phase(substance, temperature):
    if substance is None:
        return "Unknown"

    if temperature < substance["mp"]:
        return "Solid"
    elif substance["mp"] <= temperature < substance["bp"]:
        return "Liquid"
    else:
        return "Gas"

def average_kinetic_energy(temperature):
    return (3/2) * R * temperature

def imf_strength(imf):
    strengths = {
        "London Dispersion Forces": 1,
        "Dipole-Dipole": 2,
        "Hydrogen Bonding": 3,
        "Ionic Forces": 4
    }
    return strengths.get(imf, 0)
