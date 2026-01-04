import streamlit as st

st.set_page_config(
    page_title="ChemE Process Simulator",
    layout="wide",
)

st.title("🧪 Chemical Engineering Process Simulator")
st.caption("Explore AP Chemistry concepts and Chemical Engineering applications")

st.markdown("""
Welcome! This simulator is designed to help visualize key chemistry and chemical engineering concepts.  
Use the **sidebar navigation** (at the top-left) to switch between modules:

- ⚗️ **Kinetics** — Reaction rates, concentration vs time, half-lives, Maxwell-Boltzmann distribution.  
- 🔥 **Thermodynamics** — ΔG calculations, spontaneity, energy feasibility.  
- ⚖️ **Equilibrium** — Equilibrium constants, percent conversion, Le Châtelier’s Principle.  
- 🧪 **Acids & Bases** — pH changes, titration curves, process control.  
- 🌡️ **Intermolecular Forces (IMF)** — Vapor pressure, phase predictions, molecular interactions.
""")

st.markdown("---")
st.markdown("""
### How to Use:

1. Select a module from the sidebar.
2. Adjust the inputs on the sidebar for each module (temperature, concentration, etc.).
3. Observe the graphs, tables, and computed outputs.
4. Read the explanations for real-life applications and chemical engineering relevance.
""")