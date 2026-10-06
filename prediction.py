# ==========================================================
# HYBRID COMPOSITE PREDICTION SYSTEM (HCPS)
# prediction.py
#
# Engineering Prediction Module
#
# Project:
# Development of a Sustainable Hybrid Composite
# for Penetration Resistance Application
#
# Author: Daniel Thomas
# ==========================================================


# ----------------------------------------------------------
# Predict Tensile Strength
# ----------------------------------------------------------

def predict_tensile_strength(density):
    """
    Predict Tensile Strength (MPa)
    """

    tensile = 20 + (25 * density)

    return round(tensile, 3)


# ----------------------------------------------------------
# Predict Hardness
# ----------------------------------------------------------

def predict_hardness(density):
    """
    Predict Shore D Hardness
    """

    hardness = 40 + (15 * density)

    return round(hardness, 3)


# ----------------------------------------------------------
# Predict Flexural Strength
# ----------------------------------------------------------

def predict_flexural_strength(density):
    """
    Predict Flexural Strength (MPa)
    """

    flexural = 15 + (30 * density)

    return round(flexural, 3)


# ----------------------------------------------------------
# Predict Flexural Modulus
# ----------------------------------------------------------

def predict_flexural_modulus(density):
    """
    Predict Flexural Modulus (GPa)
    """

    modulus = 2.0 + (3.2 * density)

    return round(modulus, 3)


# ----------------------------------------------------------
# Predict Impact Strength
# ----------------------------------------------------------

def predict_impact_strength(density):
    """
    Predict Impact Strength (kJ/m²)
    """

    impact = 2 + (3 * density)

    return round(impact, 3)


# ----------------------------------------------------------
# Predict Compressive Strength
# ----------------------------------------------------------

def predict_compressive_strength(density):
    """
    Predict Compressive Strength (MPa)
    """

    compressive = 35 + (40 * density)

    return round(compressive, 3)


# ----------------------------------------------------------
# Predict Young's Modulus
# ----------------------------------------------------------

def predict_young_modulus(density):
    """
    Predict Young's Modulus (GPa)
    """

    modulus = 1.5 + (2.8 * density)

    return round(modulus, 3)


# ----------------------------------------------------------
# Predict Penetration Depth
# ----------------------------------------------------------

def predict_penetration_depth(density):
    """
    Lower penetration depth indicates
    better penetration resistance.
    """

    penetration = 12 - (3 * density)

    if penetration < 0:
        penetration = 0

    return round(penetration, 3)


# ----------------------------------------------------------
# Predict Penetration Resistance Index
# ----------------------------------------------------------

def predict_penetration_resistance(density):
    """
    Higher value indicates
    better penetration resistance.
    """

    resistance = density * 100

    return round(resistance, 3)


# ----------------------------------------------------------
# Predict Specific Strength
# ----------------------------------------------------------

def predict_specific_strength(density):
    """
    Specific Strength (MPa/(g/cm³))
    """

    tensile = predict_tensile_strength(density)

    if density == 0:
        return 0

    return round(tensile / density, 3)


# ----------------------------------------------------------
# Predict All Properties
# ----------------------------------------------------------

def predict_all(density):
    """
    Returns all predicted engineering
    properties as a dictionary.
    """

    return {

        "Composite Density (g/cm³)":
            round(density, 3),


        "Flexural Strength (MPa)":
            predict_flexural_strength(density),

        "Compressive Strength (MPa)":
            predict_compressive_strength(density),

        "Young's Modulus (GPa)":
            predict_young_modulus(density),

        "Flexural Modulus (GPa)":
            predict_flexural_modulus(density),

        "Impact Strength (kJ/m²)":
            predict_impact_strength(density),

        "Specific Strength":
            predict_specific_strength(density),

       
    }


# ==========================================================
# END OF FILE
# ==========================================================