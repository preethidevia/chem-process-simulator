import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

from engine.properties import (
    SUBSTANCES,
    PERIODIC_TRENDS,
    get_substance_data,
    predict_phase,
    average_kinetic_energy,
    imf_strength
)

st.set_page_config(page_title="Properties Module", layout="wide")
st.title("Properties Module")
st.caption("AP Chemistry – Units 1 & 2: Atomic & Molecular Properties")

with st.sidebar.expander("Properties Glossary"):
    st.markdown("""
- **Atomic Radius:** Size of an atom  
- **Electronegativity:** Ability to attract electrons  
- **Ionization Energy:** Energy required to remove an electron  
- **Polarity:** Unequal electron sharing  
- **Intermolecular Forces (IMF):** Attractions between molecules  
- **Hydrogen Bonding:** Strong dipole–dipole force (N, O, F)  
""")

st.sidebar.subheader("Inputs")

substance1 = st.sidebar.selectbox(
    "Primary Substance",
    ["None"] + list(SUBSTANCES.keys())
)

substance2 = st.sidebar.selectbox(
    "Comparison Substance (Optional)",
    ["None"] + list(SUBSTANCES.keys())
)

focus = st.sidebar.radio(
    "Property Focus",
    ["Atomic Properties", "Molecular Properties", "Intermolecular Forces"]
)

temperature = st.sidebar.slider(
    "Temperature (K)", 200, 800, 298
)

st.sidebar.markdown("---")

st.sidebar.subheader("Outputs")

def display_sidebar_outputs(substance_name, temp):
    if substance_name == "None":
        st.sidebar.info("No substance selected.")
        return

    data = get_substance_data(substance_name)
    phase = predict_phase(data, temp)

    st.sidebar.markdown(f"**{substance_name}**")
    st.sidebar.write(f"- Atomic Radius: {data.get('atomic_radius', 'N/A')} pm")
    st.sidebar.write(f"- Electronegativity: {data.get('electronegativity', 'N/A')}")
    st.sidebar.write(f"- Ionization Energy: {data.get('ionization_energy', 'N/A')} kJ/mol")
    st.sidebar.write(f"- Polarity: {data.get('polarity', 'N/A')}")
    st.sidebar.write(f"- Dominant IMF: {data.get('imf', 'N/A')}")
    st.sidebar.write(f"- Boiling Point: {data.get('bp', 'N/A')} K")
    st.sidebar.write(f"- Melting Point: {data.get('mp', 'N/A')} K")
    st.sidebar.write(f"- Predicted Phase: {phase}")
    st.sidebar.write(f"- Average KE: {average_kinetic_energy(temp):.2f} J/mol")

display_sidebar_outputs(substance1, temperature)
display_sidebar_outputs(substance2, temperature)

st.markdown("---")

st.sidebar.subheader("Equations")

st.sidebar.markdown(f"""
**Average Kinetic Energy**
KE_avg = (3/2)RT  
At {temperature} K → KE_avg = {average_kinetic_energy(temperature):.2f} J/mol

**Coulomb’s Law**
F = k q₁ q₂ / r²

**IMF Strength Ranking**
LDF < Dipole–Dipole < Hydrogen Bonding < Ionic Forces

**Phase Prediction (simplified)**
- T < MP → solid  
- MP ≤ T < BP → liquid  
- T ≥ BP → gas

**Constants**
- R = 8.314 J·mol⁻¹·K⁻¹
""")

st.subheader("Calculated Properties")
cols = st.columns(2)

def display_properties(substance, col):
    if substance == "None":
        col.info("No substance selected.")
        return

    data = get_substance_data(substance)
    phase = predict_phase(data, temperature)

    col.markdown(f"### {substance}")
    col.write(f"**Molar Mass:** {data['molar_mass']} g/mol")
    col.write(f"**Polarity:** {data['polarity']}")
    col.write(f"**Dominant IMF:** {data['imf']}")
    col.write(f"**Melting Point:** {data['mp']} K")
    col.write(f"**Boiling Point:** {data['bp']} K")
    col.write(f"**Predicted Phase:** {phase}")

display_properties(substance1, cols[0])
display_properties(substance2, cols[1])

col1, col2 = st.columns(2)

with col1:
    st.subheader("Periodic Trends")

    trend_y = st.selectbox(
        "Select Trend",
        ["Atomic Radius (pm)", "Electronegativity", "Ionization Energy (kJ/mol)"]
    )

    fig1, ax1 = plt.subplots()
    ax1.plot(
        PERIODIC_TRENDS["Atomic Number"],
        PERIODIC_TRENDS[trend_y],
        marker="o",
        lw=2
    )

    ax1.set_xlabel("Atomic Number")
    ax1.set_ylabel(trend_y)
    ax1.set_title(f"{trend_y} vs Atomic Number")

    st.pyplot(fig1)

    st.dataframe(PERIODIC_TRENDS)

with col2:
    st.subheader("Intermolecular Forces vs Boiling Point")

    imf_df = pd.DataFrame([
        {
            "Substance": name,
            "Boiling Point (K)": data["bp"],
            "IMF Strength": imf_strength(data["imf"]),
            "IMF Type": data["imf"]
        }
        for name, data in SUBSTANCES.items()
    ])

    fig2, ax2 = plt.subplots()

    ax2.bar(
        imf_df["Substance"],
        imf_df["Boiling Point (K)"]
    )

    ax2.set_xlabel("Substance")
    ax2.set_ylabel("Boiling Point (K)")
    ax2.set_title("Effect of Intermolecular Forces on Boiling Point")
    ax2.tick_params(axis="x", rotation=45)

    st.pyplot(fig2)
    st.dataframe(imf_df)

st.header("Properties Concepts")

st.markdown(f"""
### Atomic Structure & Periodic Trends
Across a period, atomic radius **decreases** due to increasing effective nuclear charge.
Ionization energy and electronegativity **increase** for the same reason.

### Bonding & Polarity
Polarity depends on:
- Electronegativity difference
- Molecular geometry

Symmetrical molecules can be nonpolar even with polar bonds.

### Chemical Engineering Context
- Determines **phase behavior**
- Explains **volatility**
- Guides **separation processes**
- Predicts **material handling constraints**
""")

st.markdown("""
### Connection to Intermolecular Forces
- Atomic size and electronegativity determine **IMF type and strength**
- Stronger IMFs lead to **higher boiling points and lower vapor pressure**
- Molecular properties explain **phase behavior and physical trends**
""")