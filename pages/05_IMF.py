import streamlit as st
import matplotlib.pyplot as plt
from engine import imf

st.set_page_config(page_title="IMF Module", layout="wide")
st.title("🌡️ Intermolecular Forces & Phase Behavior")

# -------------------------------
# Sidebar Inputs
# -------------------------------
st.sidebar.subheader("IMF Inputs")
temperature = st.sidebar.slider("Temperature (K)", 200, 500, 298)
pressure = st.sidebar.slider("Pressure (atm)", 0.5, 20.0, 1.0)

# -------------------------------
# Calculations
# -------------------------------
temp_range, vapor_pressure = imf.vapor_pressure_curve()
phase = imf.phase_prediction(temperature, pressure)

# -------------------------------
# Graph
# -------------------------------
st.subheader("📈 Vapor Pressure vs Temperature")
fig, ax = plt.subplots()
ax.plot(temp_range, vapor_pressure)
ax.set_xlabel("Temperature (K)")
ax.set_ylabel("Vapor Pressure (atm)")
st.pyplot(fig)

# -------------------------------
# Outputs
# -------------------------------
st.sidebar.subheader("IMF Outputs")
st.sidebar.write("Predicted Phase:", phase)

# -------------------------------
# Explanation
# -------------------------------
st.markdown("""
**AP Chemistry Concept:**  
- Stronger intermolecular forces → lower vapor pressure  
- Weaker forces → higher vapor pressure  

**ChemE Application:**  
- Distillation column design  
- Phase separation in reactors  
- Optimizing pressure and temperature for process efficiency
""")
