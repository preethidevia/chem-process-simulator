import numpy as np

R = 8.314  # J/mol·K


# ------------------ KINETICS ------------------
def reaction_rate(T, A=1e7, Ea=80000):
    """Arrhenius equation"""
    return A * np.exp(-Ea / (R * T))


def concentration_vs_time(rate, C0=1.0, t_end=50, steps=100):
    t = np.linspace(0, t_end, steps)
    C = C0 * np.exp(-rate * t)
    return t, C


# ------------------ THERMODYNAMICS ------------------
def gibbs_free_energy(delta_H, delta_S, T):
    return delta_H - T * delta_S


def energy_cost(delta_H, conversion):
    return abs(delta_H) * conversion


# ------------------ EQUILIBRIUM ------------------
def equilibrium_constant(delta_G, T):
    return np.exp(-delta_G / (R * T))


def yield_from_equilibrium(K):
    return K / (1 + K)


# ------------------ ACIDS & BASES ------------------
def calculate_pH(H_concentration):
    return -np.log10(H_concentration)


def buffer_safe(pH, min_pH=6.5, max_pH=8.5):
    return min_pH <= pH <= max_pH


# ------------------ IMF / PHASE BEHAVIOR ------------------
def phase_state(T, boiling_point=350):
    if T > boiling_point:
        return "Gas"
    return "Liquid"


# ------------------ ENGINEERING OPTIMIZATION ------------------
def find_optimal_temperature(delta_H, delta_S):
    best_T = None
    best_yield = 0

    for T in range(300, 900, 10):
        delta_G = gibbs_free_energy(delta_H, delta_S, T)
        K = equilibrium_constant(delta_G, T)
        y = yield_from_equilibrium(K)

        if y > best_yield:
            best_yield = y
            best_T = T

    return best_T, best_yield
