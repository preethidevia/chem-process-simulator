import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from engine import thermodynamics

st.set_page_config(page_title="Thermodynamics", layout="wide")
st.title("Thermodynamics Module")
st.caption("AP Chemistry Concepts → Chemical Engineering Decisions")

with st.sidebar.expander("Thermodynamics Glossary"):
    st.markdown("""
- **Enthalpy (ΔH):** Heat absorbed or released
- **Endothermic:** ΔH > 0 (absorbs heat)
- **Exothermic:** ΔH < 0 (releases heat)
- **Activation Energy (Ea):** Energy barrier
- **Transition State:** Highest-energy point
- **Reaction Coordinate:** Progress of reaction
- **Catalyst:** Lowers Ea, not ΔH
- **Intermediate:** Temporary species
- **Heat Curve:** Temperature vs heat flow
""")

st.sidebar.subheader("Reaction Selection")

reactant1 = st.sidebar.selectbox("Reactant 1", thermodynamics.SPECIES.keys())
reactant2 = st.sidebar.selectbox("Reactant 2", thermodynamics.SPECIES.keys())
product1 = st.sidebar.selectbox("Product 1", thermodynamics.SPECIES.keys())
product2 = st.sidebar.selectbox("Product 2", thermodynamics.SPECIES.keys())

temperature = st.sidebar.slider("Temperature (K)", 250, 10000, 1000)

Ea_forward = st.sidebar.slider(
    "Forward Activation Energy (kJ/mol)", 20, 300, 120
) * 1000

has_intermediate = st.sidebar.checkbox("Reaction has intermediate")
catalyst = st.sidebar.checkbox("Catalyst present")

st.sidebar.info(
    "💧 Water is shown with a realistic heating curve because its phase-change "
    "behavior (melting and boiling) is well-known. Other substances are currently "
    "modeled as single-phase materials with no phase transitions."
)

reactants = [reactant1, reactant2]
products = [product1, product2]

delta_h = thermodynamics.reaction_enthalpy(reactants, products)

x, energy_profile, Ea_effective, E_ts = thermodynamics.reaction_profile(
    delta_h, Ea_forward, has_intermediate, catalyst
)

selected_substance = "Water (H2O)"

if product2 != "None":
    selected_substance = product2
elif product1 != "None":
    selected_substance = product1
elif reactant2 != "None":
    selected_substance = reactant2
elif reactant1 != "None":
    selected_substance = reactant1

heat_q, temp_curve = thermodynamics.substance_heating_curve(
    selected_substance, temperature
)

st.sidebar.subheader("Thermodynamics Outputs")

st.sidebar.metric("ΔH (kJ/mol)", f"{delta_h/1000:.2f}")

reaction_type = "Endothermic" if delta_h > 0 else "Exothermic" if delta_h < 0 else "Neutral"
st.sidebar.metric("Reaction Type", reaction_type)

st.sidebar.metric("Activation Energy Ea (kJ/mol)", f"{Ea_effective/1000:.1f}")

st.sidebar.metric(
    "Transition State Energy",
    f"{E_ts/1000:.1f} kJ/mol",
)

if catalyst:
    st.sidebar.success("Catalyst lowers activation energy")
if has_intermediate:
    st.sidebar.info("Intermediate present in energy profile")

st.subheader("Reaction Energy Profile")

fig1, ax1 = plt.subplots()
ax1.plot(x, energy_profile / 1000, lw=2)

ax1.axhline(0, linestyle="--", color="gray", label="Reactants")
ax1.axhline(delta_h / 1000, linestyle="--", color="green", label="Products")

if delta_h > 0:
    ax1.text(0.6, max(energy_profile)/1000 * 0.9, "Endothermic", color="red")
elif delta_h < 0:
    ax1.text(0.6, max(energy_profile)/1000 * 0.9, "Exothermic", color="blue")
else:
    ax1.text(0.6, max(energy_profile)/1000 * 0.9, "Neutral", color="black")

ax1.set_xlabel("Reaction Coordinate")
ax1.set_ylabel("Potential Energy (kJ/mol)")
ax1.set_title("Reaction Energy Diagram")
ax1.legend()
st.pyplot(fig1)

st.dataframe({
    "Reaction Coordinate": x,
    "Potential Energy (kJ/mol)": energy_profile / 1000
})

st.subheader("Heat Curve")

fig2, ax2 = plt.subplots()
ax2.plot(heat_q / 1000, temp_curve, lw=2, color="orange")
ax2.set_xlabel("Heat Energy (kJ)")
ax2.set_ylabel("Temperature (K)")
ax2.set_title(f"Heating Curve — {selected_substance}")
st.pyplot(fig2)

st.dataframe({
    "Heat Added (kJ)": heat_q / 1000,
    "Temperature (K)": temp_curve
})

st.info(
    "Heating curves show how temperature changes as heat is added. "
    "Flat regions indicate phase changes where energy breaks intermolecular forces "
    "instead of raising temperature."
)

st.sidebar.markdown("""
### Equations

**Reaction Enthalpy**
ΔH = ΣH(products) − ΣH(reactants)

**Arrhenius Relation**
Higher Ea → slower reaction

**Single Phase Heating:**
q = m·c·ΔT

**Phase Change (Plateau):**
q = m·ΔH

Where:
- q = heat (J)
- m = mass (g)
- c = specific heat (J/g·K)
- ΔT = temperature change (K)
- ΔH = latent heat (fusion or vaporization)
""")

st.markdown("""
### Why Water Is Special Here
Water’s heating curve includes:
- Solid → liquid → gas transitions
- Large ΔH_vap due to hydrogen bonding
- Clear plateaus at phase changes

Other substances are currently shown using a **simplified model** without phase transitions due to missing thermodynamic data.
""")

st.markdown("""
## Thermodynamics Interpretation

### Reaction Energy Profile
- Peak = **transition state**
- Height = **activation energy**
- Difference between products and reactants = **ΔH**
- Catalyst lowers Ea but does **not** change ΔH
- Intermediates create multiple peaks

### Heat Curve
- Shows how **temperature changes as heat is added**
- Endothermic: temperature rises with heat input
- Exothermic: temperature drops as heat is released

## Chemical Engineering Context

- Determines **energy cost** of reactors
- Guides **catalyst selection**
- Predicts **thermal runaway risks**
- Critical for **heat exchanger design**
""")

st.markdown("""
### Connection to Kinetics

- Higher temperature → higher average kinetic energy
- More molecules exceed activation energy
- Reaction rate increases (Arrhenius relationship)

Thermodynamics explains **energy flow**, while kinetics explains **reaction speed**.
""")