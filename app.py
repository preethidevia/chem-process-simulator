#Temperature slider
#Pressure slider
#Initial concentration inputs
#Reaction selection dropdown

import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

from engine import (
    kinetics,
    thermodynamics,
    equilibrium,
    acids_bases,
    imf
)

st.set_page_config(page_title="ChemE Process Simulator", layout="wide")
st.title("🧪 Chemical Engineering Process Simulator")
st.caption("AP Chemistry Concepts → Chemical Engineering Decisions")

# ======================================
# GLOBAL CONTROLS
# ======================================
st.sidebar.header("Global Process Conditions")

temperature = st.sidebar.slider("Temperature (K)", 250, 1000, 500)
pressure = st.sidebar.slider("Pressure (atm)", 1, 20, 5)
initial_conc = st.sidebar.slider("Initial Concentration (M)", 0.1, 2.0, 1.0)

reaction_type = st.sidebar.selectbox(
    "Reaction Type",
    ["First Order", "Second Order"]
)

# ======================================
# KINETICS
# ======================================
st.header("⏱️ Reaction Kinetics (AP Chem → Reactor Design)")

compound = st.selectbox(
    "Select Reactant",
    ["Generic A", "Hydrogen Peroxide", "Nitrogen Dioxide"]
)

order = st.selectbox(
    "Reaction Order",
    ["Zeroth Order", "First Order", "Second Order"]
)

time = np.linspace(0, 50, 200)

# Compute concentration
if order == "Zeroth Order":
    conc = kinetics.zeroth_order_concentration(
        initial_conc, temperature, time, compound
    )
    k = kinetics.arrhenius_rate(temperature, compound)
    half_life = kinetics.zeroth_order_half_life(initial_conc, k)

elif order == "First Order":
    conc = kinetics.first_order_concentration(
        initial_conc, temperature, time, compound
    )
    k = kinetics.arrhenius_rate(temperature, compound)
    half_life = kinetics.first_order_half_life(k)

else:
    conc = kinetics.second_order_concentration(
        initial_conc, temperature, time, compound
    )
    k = kinetics.arrhenius_rate(temperature, compound)
    half_life = kinetics.second_order_half_life(initial_conc, k)

# Plot
fig, ax = plt.subplots()
ax.plot(time, conc)
ax.set_xlabel("Time")
ax.set_ylabel("Concentration (M)")
ax.set_title(f"{order} Reaction — {compound}")
st.pyplot(fig)

# Data table
st.subheader("📊 Concentration Data")
data = {
    "Time": time,
    "Concentration (M)": conc
}
st.dataframe(data)

# Half-life display
st.metric("Half-Life", f"{half_life:.2f} time units")

st.markdown("""
### 📐 Governing Equations
- **Zeroth Order:** `[A] = [A₀] − kt`
- **First Order:** `ln[A] = −kt + ln[A₀]`
- **Second Order:** `1/[A] = kt + 1/[A₀]`

### 🧠 What This Means in Real Life
- **Zeroth Order:** Rate limited by surface or catalyst  
- **First Order:** Constant half-life (radioactive decay, gas reactions)  
- **Second Order:** Rate depends heavily on concentration  

### 🏭 Chemical Engineering Insight
Reaction order determines:
- Reactor size  
- Throughput  
- Safety margins  
- Cost efficiency  
""")

# ======================================
# THERMODYNAMICS
# ======================================
st.header("🔥 Thermodynamics (Energy Feasibility)")

delta_h = st.slider("ΔH (kJ/mol)", -150.0, 150.0, -50.0)
delta_s = st.slider("ΔS (J/mol·K)", -200.0, 200.0, -80.0)

delta_g, spontaneous = thermodynamics.gibbs_energy(delta_h, delta_s, temperature)

st.metric("ΔG (kJ/mol)", round(delta_g, 2))
st.write("Spontaneous?" , "✅ Yes" if spontaneous else "❌ No")

st.markdown("""
**Equation:**  
ΔG = ΔH − TΔS

**Real Meaning:**  
Determines whether a process is energetically worth running at scale.
""")

# ======================================
# EQUILIBRIUM
# ======================================
st.header("⚖️ Equilibrium & Yield Optimization")

K = equilibrium.equilibrium_constant(delta_h, temperature)
conversion = equilibrium.percent_conversion(K)

st.metric("Equilibrium Constant (K)", round(K, 3))
st.metric("Percent Conversion (%)", round(conversion, 1))

st.markdown("""
**Le Châtelier’s Principle:**  
Temperature and pressure shifts affect yield.

**ChemE Use:**  
Maximize product while minimizing energy & cost.
""")

# ======================================
# ACIDS & BASES
# ======================================
st.header("🧪 Acids & Bases (Process Control)")

acid_added = st.slider("Acid/Base Added (mol)", -0.5, 0.5, 0.0)
pH = acids_bases.calculate_pH(acid_added)

st.metric("pH", round(pH, 2))

curve_x, curve_y = acids_bases.titration_curve()

fig, ax = plt.subplots()
ax.plot(curve_x, curve_y)
ax.axhline(7, linestyle="--")
ax.set_xlabel("Added Base (mol)")
ax.set_ylabel("pH")
st.pyplot(fig)

st.markdown("""
**Key Rule:**  
At half-equivalence → pH = pKa

**ChemE Meaning:**  
Maintains safe operating conditions in reactors and pipelines.
""")

# ======================================
# INTERMOLECULAR FORCES
# ======================================
st.header("🌡️ Intermolecular Forces & Phase Behavior")

temp_range, vapor_pressure = imf.vapor_pressure_curve()

fig, ax = plt.subplots()
ax.plot(temp_range, vapor_pressure)
ax.set_xlabel("Temperature (K)")
ax.set_ylabel("Vapor Pressure")
st.pyplot(fig)

phase = imf.phase_prediction(temperature, pressure)

st.write("Predicted Phase:", phase)

st.markdown("""
**AP Chem:**  
Stronger IMFs → lower vapor pressure.

**ChemE:**  
Used in distillation & separation design.
""")
