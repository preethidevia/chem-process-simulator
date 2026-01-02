import streamlit as st
from engine import thermodynamics

st.set_page_config(page_title="Thermodynamics Module", layout="wide")
st.title("🔥 Thermodynamics Module")

# -------------------------------
# Sidebar Inputs
# -------------------------------
st.sidebar.subheader("Thermodynamics Inputs")
delta_h = st.sidebar.slider("ΔH (kJ/mol)", -150.0, 150.0, -50.0)
delta_s = st.sidebar.slider("ΔS (J/mol·K)", -200.0, 200.0, -80.0)
temperature = st.sidebar.slider("Temperature (K)", 250, 2000, 298)

# -------------------------------
# Calculations
# -------------------------------
delta_g, spontaneous = thermodynamics.gibbs_energy(delta_h, delta_s, temperature)

# -------------------------------
# Sidebar Outputs
# -------------------------------
st.sidebar.subheader("Thermodynamics Outputs")
st.sidebar.metric("ΔG (kJ/mol)", round(delta_g, 2))
st.sidebar.write("Spontaneous?", "✅ Yes" if spontaneous else "❌ No")

st.markdown("""
**Equation Used:**  
ΔG = ΔH − TΔS

**Interpretation:**  
- ΔG < 0 → spontaneous  
- ΔG > 0 → non-spontaneous  

**ChemE Insight:**  
Helps determine whether a reaction is energetically feasible at a given temperature and informs process design and energy efficiency.
""")
