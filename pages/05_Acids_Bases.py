import streamlit as st
import matplotlib.pyplot as plt

from engine.acids_bases import *

st.set_page_config(page_title="Acids & Bases", layout="wide")

st.title("Acids & Bases")

with st.sidebar.expander("Acids & Bases Glossary"):
    st.markdown("""
- **Acid**: Proton (H⁺) donor  
- **Base**: Proton (H⁺) acceptor  
- **Strong Acid/Base**: Fully dissociates  
- **Weak Acid/Base**: Partially dissociates  
- **Titration**: Controlled acid–base reaction  
- **Equivalence Point**: Moles acid = moles base  
- **Indicator**: Signals equivalence  
- **pH**: Measure of acidity  
- **Absorbance**: Light absorbed by solution  
""")

st.sidebar.header("Inputs")

acid_molarity = st.sidebar.slider(
    "Acid Molarity (M)", 0.1, 2.0, 1.0
)

acid_volume = st.sidebar.slider(
    "Analyte Volume (L)", 0.01, 0.10, 0.05
)

base_molarity = st.sidebar.slider(
    "Titrant Molarity (M)", 0.1, 2.0, 1.0
)

base_volume = st.sidebar.slider(
    "Titrant Volume Added (L)", 0.0, 0.10, 0.05
)

outputs = calculate_outputs(
    acid_molarity,
    acid_volume,
    base_molarity,
    base_volume
)

titration_df, equivalence_volume = generate_titration_curve(
    acid_molarity,
    acid_volume,
    base_molarity,
    max_base_volume=0.10
)

absorbance_df = generate_absorbance_data(
    concentration_max=acid_molarity
)

st.sidebar.header("Outputs")

st.sidebar.metric(
    "Analyte Concentration (M)",
    f"{outputs['Analyte Concentration (M)']:.3f}"
)

st.sidebar.metric(
    "pH",
    f"{outputs['pH']:.2f}"
)

st.sidebar.metric(
    "Absorbance",
    f"{outputs['Absorbance']:.2f}"
)

st.sidebar.markdown(f"""
**Equations**
- M_1 V_1 = M_2 V_2
- pH = -log[H⁺]
- A = ε b c

**Constants**
- ε = 100 L/mol·cm
- b = 1 cm
""")

col1, col2 = st.columns(2)

with col1:
    st.subheader("Titration Curve")

    fig, ax = plt.subplots()
    ax.plot(
        titration_df["Volume of Titrant Added (L)"],
        titration_df["pH"]
    )
    ax.axvline(
        equivalence_volume,
        linestyle="--",
        label="Equivalence Point"
    )
    ax.set_xlabel("Volume of Titrant Added (L)")
    ax.set_ylabel("pH")
    ax.legend()

    st.pyplot(fig)

    st.dataframe(titration_df)

with col2:
    st.subheader("Absorbance vs Concentration")

    fig, ax = plt.subplots()
    ax.plot(
        absorbance_df["Concentration (M)"],
        absorbance_df["Absorbance"]
    )
    ax.set_xlabel("Concentration (M)")
    ax.set_ylabel("Absorbance")

    st.pyplot(fig)

    st.dataframe(absorbance_df)

st.header("Conceptual Explanations")

st.markdown("""
### Titration
Titration is used to determine the concentration of an unknown solution by
reacting it with a solution of known concentration. The equivalence point
occurs when moles of acid equal moles of base. Observe relationships 
between various volumes and molarities in the titration curve graph.

### Strong vs Weak Acids and Bases
Strong acids and bases fully dissociate, causing sharp pH changes near
equivalence. Weak acids and bases form buffer regions.

### Absorbance & Spectroscopy
Absorbance follows the Beer–Lambert Law, showing a linear relationship between
concentration and absorbance. This method is commonly used to determine
unknown concentrations in solution.

### Chemical Engineering Context
- pH control is critical for **reaction yield, safety, and product quality**
- Titration curves determine **concentration and stoichiometric completion**
- Absorbance enables **real-time monitoring** of analyte concentration
""")
