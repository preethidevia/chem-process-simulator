import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from engine import kinetics

st.set_page_config(page_title="Kinetics Module", layout="wide")
st.title("⚗️ Kinetics Module")

# -------------------------------
# Sidebar Inputs
# -------------------------------
st.sidebar.subheader("Kinetics Inputs")
compound = st.sidebar.selectbox("Select Reactant", list(kinetics.COMPOUNDS.keys()))
order = st.sidebar.selectbox("Reaction Order", ["Zeroth Order", "First Order", "Second Order"])
temperature = st.sidebar.slider("Temperature (K)", 250, 20000, 1000)
initial_conc = st.sidebar.slider("Initial Concentration (M)", 0.1, 10.0, 1.0)

# -------------------------------
# Compute Kinetics
# -------------------------------
time = np.linspace(0, 50, 300)
k = kinetics.arrhenius_rate(temperature, compound)

if order == "Zeroth Order":
    conc = kinetics.zeroth_order_concentration(initial_conc, temperature, time, compound)
    half_life = kinetics.zeroth_order_half_life(initial_conc, k)
    y = conc
    y_label = "[A] (M)"
    rate_law = "Rate = k"
    half_life_eq = "[A]₀ / k"
elif order == "First Order":
    conc = kinetics.first_order_concentration(initial_conc, temperature, time, compound)
    half_life = kinetics.first_order_half_life(k)
    y = np.log(np.clip(conc, 1e-12, None))
    y_label = "ln[A]"
    rate_law = "Rate = k[A]"
    half_life_eq = "ln(2)/k"
else:
    conc = kinetics.second_order_concentration(initial_conc, temperature, time, compound)
    half_life = kinetics.second_order_half_life(initial_conc, k)
    y = 1 / conc
    y_label = "1/[A] (1/M)"
    rate_law = "Rate = k[A]^2"
    half_life_eq = "1/(k[A]₀)"

# -------------------------------
# Sidebar Outputs
# -------------------------------
Ea = kinetics.COMPOUNDS[compound].get("Ea", None)
st.sidebar.subheader("Kinetics Outputs")
st.sidebar.metric("Rate Constant k", f"{k:.2e} s⁻¹")
st.sidebar.metric("Half-Life", f"{half_life:.2e} units")
st.sidebar.metric("Activation Energy Ea", f"{Ea:.2e} J/mol" if Ea else "N/A")

# Half-life notes
if order == "Zeroth Order":
    st.sidebar.info("⚡ Half-life decreases as concentration decreases (0th order).")
elif order == "First Order":
    st.sidebar.info("⚡ Half-life constant (1st order).")
else:
    st.sidebar.info("⚡ Half-life increases as concentration decreases (2nd order).")

st.sidebar.markdown(f"""
**Equations Used:**

- Rate Law: {rate_law}
- Zeroth Order: [A] = [A₀] − kt
- First Order: ln[A] = −kt + ln[A₀]
- Second Order: 1/[A] = kt + 1/[A₀]
- Half-Life Equation: {half_life_eq}

**Constants:**
- R = 8.314 J/mol·K
""")

# -------------------------------
# Concentration vs Time Graph
# -------------------------------
st.subheader("📈 Concentration vs Time")
fig, ax = plt.subplots()
ax.plot(time, y, color="#1f77b4", lw=2)
ax.set_xlabel("Time")
ax.set_ylabel(y_label)
ax.set_title(f"{order} Reaction — {compound}")
ax.axvline(half_life, color="red", linestyle="--", label="Half-Life")
ax.legend()
st.pyplot(fig)

# -------------------------------
# Data Table
# -------------------------------
st.subheader("📊 Data Points")
st.dataframe({"Time": time, y_label: y})

# -------------------------------
# Maxwell-Boltzmann Graph
# -------------------------------
st.subheader("⚡ Molecules vs Kinetic Energy (MB Distribution)")
mass = kinetics.COMPOUNDS[compound].get("mass", 5e-26)
KE, f_v = kinetics.maxwell_boltzmann_distribution(temperature, mass)

fig2, ax2 = plt.subplots(figsize=(7,4))
ax2.plot(KE, f_v, lw=2, color="blue")
if Ea:
    ax2.axvline(Ea, color="red", lw=2, linestyle="--", label="Ea")
    ax2.fill_between(KE, 0, f_v, where=(KE>=Ea), color="orange", alpha=0.4, label="Molecules ≥ Ea")
    ax2.legend()

ax2.set_xlabel("Kinetic Energy (J)")
ax2.set_ylabel("Fraction of Molecules")
ax2.set_title(f"{compound} — MB Distribution at {temperature} K")
ax2.set_xlim([0, max(KE)*1.05])
ax2.set_ylim([0,1.05])
st.pyplot(fig2)

# -------------------------------
# Fraction reactive note
# -------------------------------
fraction_reactive = np.sum(f_v[KE>=Ea])/np.sum(f_v) if Ea else 0
if fraction_reactive < 0.05:
    st.warning(f"⚠ Only {fraction_reactive*100:.1f}% of molecules exceed Ea. Increase temperature to accelerate.")
elif fraction_reactive < 0.2:
    st.info(f"💡 About {fraction_reactive*100:.1f}% exceed Ea. Reaction will be slow.")
else:
    st.success(f"✅ {fraction_reactive*100:.1f}% exceed Ea. Reaction likely efficient.")

# -------------------------------
# Explanations
# -------------------------------
st.markdown("""
### 📐 Real-Life Graph Interpretation
- Zeroth Order: Rate independent of concentration. Linear decrease.
- First Order: Half-life constant, typical for radioactive decay.
- Second Order: Rate depends on [A]^2, e.g., dimerization.

### 🧠 Half-Life
- Zeroth: t₁/₂ = [A]₀ / k
- First: t₁/₂ = ln(2)/k
- Second: t₁/₂ = 1/(k[A]₀)

### ⚡ Maxwell-Boltzmann
- Vertical line = Ea
- Area right of line = fraction of molecules energetic enough to react
- Higher T → more molecules surpass Ea → faster reactions

### 🏭 Chemical Engineering Insight
- Reaction order affects reactor design and throughput
- Temperature affects reactive molecule fraction
- Nuclear isotopes are always 1st order; incompatible orders show warnings
""")
