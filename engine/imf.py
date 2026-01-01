#Implement:
#Vapor pressure estimation
#Phase prediction
#Solvent effects
#Outputs:
#Phase (gas/liquid)
#Separation feasibility
#AP Chem: IMFs
#ChemE: Materials & separation

def phase_state(T, boiling_point=350):
    if T > boiling_point:
        return "Gas"
    return "Liquid"

def explain_imf():
    return ("Intermolecular forces (IMFs) affect phase behavior, "
            "boiling point, and solvent selection. Weak IMFs = easier to vaporize.")

def optimize_phase(boiling_point=350, T_min=300, T_max=900):
    """
    Suggests temperature closest to desired phase (liquid or gas)
    """
    if T_min <= boiling_point <= T_max:
        return boiling_point, phase_state(boiling_point, boiling_point)
    else:
        return T_min, phase_state(T_min, boiling_point)
