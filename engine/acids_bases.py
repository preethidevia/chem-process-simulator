import numpy as np
import pandas as pd
import math

KW = 1e-14  # water equilibrium constant
DEFAULT_EPSILON = 100  # L/(mol·cm)
PATH_LENGTH = 1  # cm

def calculate_moles(M, V):
    return M * V

def calculate_ph_strong_acid(moles_acid, moles_base, total_volume):
    excess_h = moles_acid - moles_base

    if excess_h > 0:
        h_conc = excess_h / total_volume
        return -math.log10(h_conc)
    elif excess_h < 0:
        oh_conc = abs(excess_h) / total_volume
        poh = -math.log10(oh_conc)
        return 14 - poh
    else:
        return 7.0

def generate_titration_curve(
    acid_molarity,
    acid_volume,
    base_molarity,
    max_base_volume,
    points=50
):
    volumes = np.linspace(0, max_base_volume, points)
    ph_values = []

    initial_moles_acid = calculate_moles(acid_molarity, acid_volume)

    for Vb in volumes:
        moles_base = calculate_moles(base_molarity, Vb)
        total_volume = acid_volume + Vb

        ph = calculate_ph_strong_acid(
            initial_moles_acid,
            moles_base,
            total_volume
        )
        ph_values.append(ph)

    df = pd.DataFrame({
        "Volume of Titrant Added (L)": volumes,
        "pH": ph_values
    })

    equivalence_volume = initial_moles_acid / base_molarity

    return df, equivalence_volume

def generate_absorbance_data(
    concentration_max,
    epsilon=DEFAULT_EPSILON,
    path_length=PATH_LENGTH,
    points=20
):
    concentrations = np.linspace(0, concentration_max, points)
    absorbance = epsilon * path_length * concentrations

    df = pd.DataFrame({
        "Concentration (M)": concentrations,
        "Absorbance": absorbance
    })

    return df

def calculate_outputs(
    acid_molarity,
    acid_volume,
    base_molarity,
    base_volume
):
    moles_acid = calculate_moles(acid_molarity, acid_volume)
    moles_base = calculate_moles(base_molarity, base_volume)

    total_volume = acid_volume + base_volume

    ph = calculate_ph_strong_acid(
        moles_acid,
        moles_base,
        total_volume
    )

    analyte_concentration = moles_acid / acid_volume
    absorbance = DEFAULT_EPSILON * PATH_LENGTH * analyte_concentration

    return {
        "Analyte Concentration (M)": analyte_concentration,
        "pH": ph,
        "Absorbance": absorbance
    }
