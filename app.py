#Temperature slider
#Pressure slider
#Initial concentration inputs
#Reaction selection dropdown

import streamlit as st
import matplotlib.pyplot as plt

from engine import (
    reaction_rate,
    concentration_vs_time,
    gibbs_free_energy,
    energy_cost,
    equilibrium_constant,
    yield_from_equilibrium,
    calculate_pH,
    buffer_safe,
    phase_state,
    find_optimal_temperature,
)

st.set_page_config(page_title="Chemical Process Simulator", layout="wide")

st.title("Computational Chemical Process Simulator")
st.write(
    "This web app models a simplified chemical process using AP Chemistry principles "
    "and chemical engineering decision-making."
)

# ------------------ USER INPUTS ------------------
st.sidebar.header("Operating Conditions")

temperature = st.sidebar.slider("Temperature (K)", 300, 900, 500)
pressure = st.sidebar.slider("Pressure (atm)", 1, 50, 10)
initial_concentration = st.sidebar.slider("Initial Concentration (mol/L)", 0.1, 2.0, 1.0)

delta_H = st.sidebar.number_input("ΔH (J/mol)", value=-80000)
delta_S = st.sidebar.number_input("ΔS (J/mol·K)", value=-150.0)

H_conc = st.sidebar.slider("Hydrogen Ion Concentration (mol/L)", 1e-9, 1e-2, 1e-7, format="%.1e")

# ------------------ CALCULATIONS ------------------
rate = reaction_rate(temperature)
t, C = concentration_vs_time(rate, initial_concentration)

delta_G = gibbs_free_energy(delta_H, delta_S, temperature)
K = equilibrium_constant(delta_G, temperature)
yield_percent = yield_from_equilibrium(K) * 100

energy = energy_cost(delta_H, yield_percent / 100)
pH = calculate_pH(H_conc)
safe_buffer = buffer_safe(pH)
phase = phase_state(temperature)

optimal_T, optimal_yield = find_optimal_temperature(delta_H, delta_S)

# ------------------ PLOTS ------------------
st.subheader("Reaction Behavior")

fig, ax = plt.subplots()
ax.plot(t, C)
ax.set_xlabel("Time")
ax.set_ylabel("Concentration (mol/L)")
ax.set_title("Concentration vs Time")
st.pyplot(fig)

# ------------------ ENGINEERING INSIGHT PANEL ------------------
st.header("Engineering Tradeoffs")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Reaction Rate", f"{rate:.2e}")

with col2:
    st.metric("Yield", f"{yield_percent:.1f}%")

with col3:
    st.metric("Energy Cost", f"{energy:.1f} J")

# Fast reaction vs energy
if rate > 1e3 and energy > 60000:
    st.warning("Fast reaction achieved at the cost of high energy consumption.")
elif rate < 1e2:
    st.info("Energy-efficient conditions slow down reaction rates.")
else:
    st.success("Balanced reaction speed and energy usage.")

# Yield vs safety
if yield_percent > 80 and not safe_buffer:
    st.error("High yield comes with pH instability and safety concerns.")
elif safe_buffer:
    st.success("pH is within safe operating limits.")
else:
    st.warning("Reduced yield improves process safety.")

# Optimal vs practical
st.subheader("Optimal vs Practical Conditions")

st.write(f"**Theoretical Optimal Temperature:** {optimal_T} K")
st.write(f"**User Selected Temperature:** {temperature} K")

if abs(temperature - optimal_T) < 30:
    st.success("User-selected conditions closely match the theoretical optimum.")
elif temperature < optimal_T:
    st.info("User selected safer, lower-energy operating conditions.")
else:
    st.warning("User selected aggressive conditions that may strain equipment.")

# Phase behavior
st.subheader("Phase Behavior")
st.write(f"Predicted phase at operating conditions: **{phase}**")

# ------------------ FINAL INSIGHT ------------------
st.subheader("Engineering Insight")

st.write(
    """
This simulation demonstrates that chemical engineering decisions require balancing
reaction kinetics, thermodynamics, energy efficiency, and safety.
The chemically optimal solution is often adjusted to meet real-world engineering constraints.
"""
)
