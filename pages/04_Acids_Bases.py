import streamlit as st
from engine import acids_bases
import matplotlib.pyplot as plt

st.set_page_config(page_title="Acids & Bases Module", layout="wide")
st.title("🧪 Acids & Bases Module")

# -------------------------------
# Sidebar Inputs
# -------------------------------
st.sidebar.subheader("Acid/Base Inputs")
acid_added = st.sidebar.slider("Acid/Base Added (mol)", -0.5, 0.5, 0.0)

# -------------------------------
# Calculations
# -------------------------------
pH = acids_bases.calculate_pH(acid_added)
curve_x, curve_y = acids_bases.titration_curve()

# -------------------------------
# Sidebar Outputs
# -------------------------------
st.sidebar.subheader("Outputs")
st.sidebar.metric("pH", round(pH, 2))

# -------------------------------
# Graph
# -------------------------------
st.subheader("📈 Titration Curve")
fig, ax = plt.subplots()
ax.plot(curve_x, curve_y)
ax.axhline(7, linestyle="--", color="red")
ax.set_xlabel("Added Base (mol)")
ax.set_ylabel("pH")
st.pyplot(fig)

# -------------------------------
# Explanation
# -------------------------------
st.markdown("""
**Key Rules:**  
- At half-equivalence → pH = pKa  
- Strong acid + strong base → pH neutral at equivalence

**ChemE Insight:**  
Maintains safe pH conditions in reactors and pipelines.
""")
