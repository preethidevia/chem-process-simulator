import streamlit as st
import matplotlib.pyplot as plt

from engine.imf import (
    SUBSTANCES,
    generate_potential_energy_data,
    generate_bp_mp_vs_molar_mass,
    generate_vapor_pressure_data,
    get_substance_outputs
)

st.set_page_config(page_title="Intermolecular Forces", layout="wide")

st.title("Intermolecular Forces (IMF)")

with st.sidebar.expander("IMF Glossary"):
    st.markdown("""
- **Intermolecular Forces (IMF)**: Attractions between molecules  
- **Potential Energy**: Energy due to molecular interactions  
- **Internuclear Distance**: Distance between nuclei  
- **Boiling Point**: Temp where vapor pressure equals atmospheric pressure  
- **Melting Point**: Solid → liquid transition  
- **Vapor Pressure**: Pressure of vapor above a liquid  
""")

st.sidebar.header("Inputs")

substances_selected = st.sidebar.multiselect(
    "Select Substances",
    list(SUBSTANCES.keys()),
    default=["H2O", "CH4", "CO2"]
)

temperature = st.sidebar.slider(
    "Temperature (K)", 250, 400, 298
)

st.sidebar.header("Outputs")

for s in substances_selected:
    data = get_substance_outputs(s)
    st.sidebar.markdown(f"### {s}")
    st.sidebar.write(f"Molar Mass: {data['molar_mass']} g/mol")
    st.sidebar.write(f"Melting Point: {data['melting_point']} K")
    st.sidebar.write(f"Boiling Point: {data['boiling_point']} K")
    st.sidebar.write(f"Vapor Pressure @298K: {data['vapor_pressure_298']} kPa")
    st.sidebar.write(f"Internuclear Distance: {data['internuclear_distance']} nm")

st.sidebar.markdown(f"""
### Equations

**Potential Energy Curve**
- U(r) = A/r^12 - B/r^6

**Vapor Pressure Approximation**
- P = P_0 e^k(T - 298)

**Constants**
- R = 8.314 J/mol·K
""")

col1, col2 = st.columns(2)

with col1:
    st.subheader("Potential Energy & Phase Properties")

    pe_df = generate_potential_energy_data()
    bp_df = generate_bp_mp_vs_molar_mass()

    fig, ax1 = plt.subplots()

    ax1.plot(
        pe_df["Internuclear Distance (nm)"],
        pe_df["Potential Energy"],
        color="blue",
        label="Potential Energy"
    )

    ax1.set_xlabel("Internuclear Distance (nm)")
    ax1.set_ylabel("Potential Energy")

    # fig, ax2 = plt.subplots()
    # # ax2 = ax1.twinx()
    # ax2.plot(
    #     bp_df["Molar Mass (g/mol)"],
    #     bp_df["Boiling Point (K)"],
    #     color="red",
    #     #marker="o",
    #     label="Boiling Point"
    # )

    # ax2.set_xlabel("Molar Mass (g/mol)")
    # ax2.set_ylabel("Boiling Point (K)")

    st.pyplot(fig)
    st.dataframe(pe_df)

with col2:
    st.subheader("Vapor Pressure vs Temperature")

    fig, ax = plt.subplots()

    for s in substances_selected:
        vp_df = generate_vapor_pressure_data(s)
        ax.plot(
            vp_df["Temperature (K)"],
            vp_df["Vapor Pressure (kPa)"],
            label=s
        )

    ax.set_xlabel("Temperature (K)")
    ax.set_ylabel("Vapor Pressure (kPa)")
    ax.legend()

    st.pyplot(fig)
    st.dataframe(vp_df)

st.header("Conceptual Explanations")

st.markdown("""
### Potential Energy & Internuclear Distance
As molecules approach, attractive forces lower potential energy until
repulsive forces dominate. Stronger IMFs create deeper potential wells.

### Molar Mass & Phase Changes
Higher molar mass and stronger IMFs increase boiling and melting points
because more energy is required to separate particles.

### Vapor Pressure
Substances with weaker IMFs have higher vapor pressure because molecules
escape the liquid phase more easily.

### Chemical Engineering Context
- IMFs control **boiling points, phase changes, and separations**
- Vapor pressure data guides **temperature and pressure limits**
- Molecular interactions inform **distillation and solvent selection**
""")