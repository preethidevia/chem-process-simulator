import streamlit as st
from engine import equilibrium

st.set_page_config(page_title="Equilibrium Module", layout="wide")
st.title("⚖️ Equilibrium Module")

# -------------------------------
# Sidebar Inputs
# -------------------------------
st.sidebar.subheader("Equilibrium Inputs")
delta_h = st.sidebar.slider("ΔH (kJ/mol)", -150.0, 150.0, -50.0)
temperature = st.sidebar.slider("Temperature (K)", 250, 2000, 298)

# -------------------------------
# Calculations
# -------------------------------
K = equilibrium.equilibrium_constant(delta_h, temperature)
conversion = equilibrium.percent_conversion(K)

# -------------------------------
# Sidebar Outputs
# -------------------------------
st.sidebar.subheader("Equilibrium Outputs")
st.sidebar.metric("Equilibrium Constant (K)", round(K, 3))
st.sidebar.metric("Percent Conversion (%)", round(conversion, 1))

st.markdown("""
**Interpretation:**  
- High K → favors products  
- Low K → favors reactants  

**Le Châtelier's Principle:**  
- Increasing T for endothermic reactions increases K  
- Increasing T for exothermic reactions decreases K  

**ChemE Insight:**  
Optimize product yield while minimizing energy cost and maintaining safe operating conditions.
""")
