# Computational Chemical Engineering Simulator

This project is a **modular web app** that integrates key AP Chemistry topics and demonstrates chemical engineering thinking.  

**Topics Included:**
- **Kinetics:** Arrhenius equation, reaction rate, concentration vs time, optimal temperature for fastest rate.
- **Thermodynamics:** Gibbs free energy, energy cost, temperature optimization for spontaneous reactions.
- **Equilibrium:** Equilibrium constant, yield calculation, temperature for maximum yield.
- **Acids & Bases:** pH calculation, buffer safety, optimal hydrogen ion concentration.
- **Intermolecular Forces (IMFs):** Phase prediction, impact of IMFs, temperature optimization for desired phase.


## Features

- **Kinetics Module**
  - Zeroth, First, and Second order reactions
  - Arrhenius rate constants
  - Half-life calculations
  - Concentration vs time graphs
  - Maxwell-Boltzmann distribution with activation energy
  - Nuclear decay and common elements

- **Thermodynamics**
  - ΔG computation
  - Spontaneity check

- **Equilibrium**
  - Equilibrium constant K
  - Percent conversion
  - Le Châtelier's principle effects

- **Acids & Bases**
  - pH calculation
  - Titration curves
  - Buffer effects

- **Intermolecular Forces**
  - Vapor pressure curves
  - Phase prediction

## Why This Matters
This project demonstrates how microscopic chemistry concepts
scale into industrial chemical processes.

## Tech Stack
- Python
- Streamlit
- NumPy
- Matplotlib

## How to Run Locally

```bash
git clone https://github.com/yourusername/chem-process-simulator.git
cd chem-process-simulator
python -m venv venv
venv\Scripts\activate  # Windows
source venv/bin/activate  # macOS/Linux
pip install -r requirements.txt
streamlit run app.py
