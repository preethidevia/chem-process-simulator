#Temperature slider
#Pressure slider
#Initial concentration inputs
#Reaction selection dropdown

import streamlit as st
import matplotlib.pyplot as plt

from engine import (
    reaction_rate, concentration_vs_time, optimize_rate,
    gibbs_free_energy, energy_cost, optimize_energy,
    equilibrium_constant, yield_from_equilibrium, optimize_equilibrium,
    calculate_pH, buffer_safe, optimize_pH,
    phase_state, explain_imf, optimize_phase
)

st.set_page_config(page_title="ChemE Simulator", layout="wide")
st.title("Computational Chemical Engineering Simulator")

st.write(
    "This simulator integrates AP Chemistry topics (kinetics, thermodynamics, equilibrium, "
    "acids/bases, and intermolecular forces) into an interactive web app with engineering tradeoffs."
)

# ------------------ User Inputs ------------------
st.sidebar.header("Operating Conditions")
temperature = st.sidebar.slider("Temperature (K)", 300, 900, 500)
pressure = st.sidebar.slider("Pressure (atm)", 1, 50, 10)
initial_concentration = st.sidebar.slider("Initial Concentration (mol/L)", 0.1, 2.0, 1.0)
delta_H = st.sidebar.number_input("ΔH (J/mol)", value=-80000)
delta_S = st.sidebar.number_input("ΔS (J/mol·K)", value=-150.0)
H_conc = st.sidebar.slider("Hydrogen Ion Concentration (mol/L)", 1e-9, 1e-2, 1e-7, format="%.1e")

# ------------------ Kinetics ------------------
st.subheader("Kinetics")
st.write("Reaction rate depends on temperature and activation energy (Arrhenius equation).")
rate = reaction_rate(temperature)
t, C = concentration_vs_time(rate, initial_concentration)
fig, ax = plt.subplots()
ax.plot(t, C)
ax.set_xlabel("Time")
ax.set_ylabel("Concentration (mol/L)")
st.pyplot(fig)
opt_T, opt_rate = optimize_rate()
st.write(f"Practical optimization: best T = {opt_T} K, rate = {opt_rate:.2e} 1/s")

# ------------------ Thermodynamics ------------------
st.subheader("Thermodynamics")
st.write("Gibbs free energy indicates spontaneity; energy cost affects efficiency.")
delta_G = gibbs_free_energy(delta_H, delta_S, temperature)
energy = energy_cost(delta_H, delta_G)
st.metric("ΔG (J)", f"{delta_G:.1f}")
st.metric("Energy Cost (J)", f"{energy:.1f}")
opt_T_e, opt_energy = optimize_energy(delta_H, delta_S)
st.write(f"Optimization: T = {opt_T_e} K, lowest energy while spontaneous = {opt_energy:.1f} J")

# ------------------ Equilibrium ------------------
st.subheader("Equilibrium")
st.write("Equilibrium constant determines reaction yield.")
K = equilibrium_constant(delta_G, temperature)
yield_percent = yield_from_equilibrium(K) * 100
st.metric("Yield (%)", f"{yield_percent:.1f}")
opt_T_y, opt_yield = optimize_equilibrium(delta_H, delta_S)
st.write(f"Optimization: T = {opt_T_y} K, max yield = {opt_yield*100:.1f}%")

# ------------------ Acids & Bases ------------------
st.subheader("Acids & Bases")
st.write("pH affects stability and safety; buffers maintain desired range.")
pH = calculate_pH(H_conc)
safe_buffer = buffer_safe(pH)
st.metric("pH", f"{pH:.2f}")
st.write("Safe buffer range: 6.5 – 8.5")
if safe_buffer: st.success("pH is within safe range.")
else: st.error("pH outside safe range!")
opt_H, opt_pH = optimize_pH()
st.write(f"Optimization: H+ = {opt_H:.2e}, pH = {opt_pH:.2f} (safe buffer)")

# ------------------ Intermolecular Forces ------------------
st.subheader("Intermolecular Forces (IMFs)")
st.write(explain_imf())
phase = phase_state(temperature)
st.metric("Phase", phase)
opt_T_phase, opt_phase_state = optimize_phase()
st.write(f"Optimization: T = {opt_T_phase} K, phase = {opt_phase_state}")

# ------------------ Engineering Tradeoffs ------------------
st.subheader("Engineering Tradeoffs")
st.write(
    "All modules now include optimization. Students can see how changing temperature, concentration, "
    "or pH affects rate, yield, energy cost, and phase."
)
