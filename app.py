import streamlit as st

st.set_page_config(
    page_title="ChemE Process Simulator",
    layout="wide",
)

st.title("Chemical Engineering Process Simulator")
st.caption("Explore AP Chemistry concepts and Chemical Engineering applications")

st.markdown("""
Welcome! This simulator is designed to help visualize key chemistry and chemical engineering concepts.  
Use the **sidebar navigation** (at the top-left) to switch between modules:

- **Intermolecular Forces (IMF)** — Potential energy, vapor pressure, phase properties.
- **Properties** — Periodic trends, intermolecular forces, molecular properties.  
- **Kinetics** — Reaction rates, concentration vs time, half-lives, Maxwell-Boltzmann distribution.  
- **Thermodynamics** — Reaction energy profiles, heat curves, kinetics.  
- **Acids & Bases** — pH changes, titration curves, absorbance vs concentration.  
""")

st.markdown("---")
st.markdown("""
### How to Use:

1. Select a module from the sidebar.
2. Adjust the inputs on the sidebar for each module (temperature, concentration, etc.).
3. Observe the graphs, tables, and computed outputs.
4. Read the explanations for real-life applications and chemical engineering relevance.
""")