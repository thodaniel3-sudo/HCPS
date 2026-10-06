
# ==========================================================
# HYBRID COMPOSITE PREDICTION SYSTEM (HCPS)
# calculations.py
#
# Engineering Calculation Module
#
# Project:
# Development of an Eco-Friendly Epoxy Hybrid Composite
# Reinforced with Bio-Waste for Automotive Application
# ==========================================================


# ==========================================================
# CONSTANT TOTAL COMPOSITE VOLUME
# ==========================================================

TOTAL_VOLUME = 104.0   # cm³


# ==========================================================
# VALIDATE COMPOSITION PERCENTAGES
# ==========================================================

def validate_percentages(
    epoxy_percent,
    horn_percent,
    cotton_percent,
    limestone_percent
):
    """
    Checks whether the four constituent volume percentages
    add up to exactly 100%.
    """

    total = (
        float(epoxy_percent)
        + float(horn_percent)
        + float(cotton_percent)
        + float(limestone_percent)
    )

    valid = abs(total - 100.0) < 0.001

    return valid, total


# ==========================================================
# CONVERT PERCENTAGE TO VOLUME FRACTION
# ==========================================================

def volume_fraction(percent):
    """
    Converts percentage to decimal volume fraction.

    Example:
        90% -> 0.90
        4%  -> 0.04
    """

    return float(percent) / 100.0


# ==========================================================
# CALCULATE CONSTITUENT VOLUMES
# ==========================================================

def constituent_volumes(
    total_volume,
    epoxy_percent,
    horn_percent,
    cotton_percent,
    limestone_percent
):
    """
    Calculates the volume of each constituent.

    Formula:

        Vi = volume fraction × total composite volume
    """

    total_volume = float(total_volume)

    volumes = {
        "Epoxy": volume_fraction(epoxy_percent) * total_volume,

        "Cow Horn": volume_fraction(horn_percent) * total_volume,

        "Cotton": volume_fraction(cotton_percent) * total_volume,

        "Limestone": volume_fraction(limestone_percent) * total_volume
    }

    return volumes


# ==========================================================
# CALCULATE CONSTITUENT MASSES
# ==========================================================

def constituent_masses(
    epoxy_density,
    horn_density,
    cotton_density,
    limestone_density,
    volumes
):
    """
    Calculates constituent masses.

    Formula:

        Mass = Density × Volume
    """

    masses = {
        "Epoxy":
            float(epoxy_density) * volumes["Epoxy"],

        "Cow Horn":
            float(horn_density) * volumes["Cow Horn"],

        "Cotton":
            float(cotton_density) * volumes["Cotton"],

        "Limestone":
            float(limestone_density) * volumes["Limestone"]
    }

    return masses


# ==========================================================
# DIRECT RULE OF MIXTURES
# ==========================================================

def composite_density(
    epoxy_density,
    horn_density,
    cotton_density,
    limestone_density,
    epoxy_percent,
    horn_percent,
    cotton_percent,
    limestone_percent,
    total_volume=TOTAL_VOLUME
):
    """
    Calculates theoretical composite density using the
    DIRECT VOLUME-FRACTION RULE OF MIXTURES.

    Formula:

    ρc = Veρe + Vhρh + Vcottonρcotton + Vlρl

    where:

        Ve       = epoxy volume fraction
        Vh       = cow horn volume fraction
        Vcotton  = cotton wool volume fraction
        Vl       = limestone volume fraction

    IMPORTANT:
    The percentages supplied to this function are VOLUME
    PERCENTAGES, not mass percentages.

    The total volume is used for mass/volume verification,
    but it does not change the theoretical density when
    the volume fractions remain constant.
    """

    # ------------------------------------------------------
    # Convert all inputs to floating-point numbers
    # ------------------------------------------------------

    epoxy_density = float(epoxy_density)
    horn_density = float(horn_density)
    cotton_density = float(cotton_density)
    limestone_density = float(limestone_density)

    epoxy_percent = float(epoxy_percent)
    horn_percent = float(horn_percent)
    cotton_percent = float(cotton_percent)
    limestone_percent = float(limestone_percent)

    total_volume = float(total_volume)

    # ------------------------------------------------------
    # Validate percentages
    # ------------------------------------------------------

    valid, total = validate_percentages(
        epoxy_percent,
        horn_percent,
        cotton_percent,
        limestone_percent
    )

    if not valid:
        raise ValueError(
            f"Composition percentages must equal 100%. "
            f"Current total = {total:.3f}%"
        )

    # ------------------------------------------------------
    # Convert percentages to volume fractions
    # ------------------------------------------------------

    Ve = epoxy_percent / 100.0
    Vh = horn_percent / 100.0
    Vcotton = cotton_percent / 100.0
    Vl = limestone_percent / 100.0

    # ------------------------------------------------------
    # DIRECT RULE OF MIXTURES
    # ------------------------------------------------------

    density = (
        Ve * epoxy_density
        + Vh * horn_density
        + Vcotton * cotton_density
        + Vl * limestone_density
    )

    return density


# ==========================================================
# COMPLETE RULE-OF-MIXTURES CALCULATION
# ==========================================================

def rule_of_mixtures_calculation(
    epoxy_density,
    horn_density,
    cotton_density,
    limestone_density,
    epoxy_percent,
    horn_percent,
    cotton_percent,
    limestone_percent,
    total_volume=TOTAL_VOLUME
):
    """
    Performs the complete Rule-of-Mixtures calculation.

    Returns:

        volumes
        masses
        total mass
        total volume
        theoretical density
    """

    # ------------------------------------------------------
    # Convert inputs to float
    # ------------------------------------------------------

    epoxy_density = float(epoxy_density)
    horn_density = float(horn_density)
    cotton_density = float(cotton_density)
    limestone_density = float(limestone_density)

    epoxy_percent = float(epoxy_percent)
    horn_percent = float(horn_percent)
    cotton_percent = float(cotton_percent)
    limestone_percent = float(limestone_percent)

    total_volume = float(total_volume)

    # ------------------------------------------------------
    # Validate percentages
    # ------------------------------------------------------

    valid, total = validate_percentages(
        epoxy_percent,
        horn_percent,
        cotton_percent,
        limestone_percent
    )

    if not valid:
        raise ValueError(
            f"Composition percentages must equal 100%. "
            f"Current total = {total:.3f}%"
        )

    # ------------------------------------------------------
    # Calculate constituent volumes
    # ------------------------------------------------------

    volumes = constituent_volumes(
        total_volume,
        epoxy_percent,
        horn_percent,
        cotton_percent,
        limestone_percent
    )

    # ------------------------------------------------------
    # Calculate constituent masses
    # ------------------------------------------------------

    masses = constituent_masses(
        epoxy_density,
        horn_density,
        cotton_density,
        limestone_density,
        volumes
    )

    # ------------------------------------------------------
    # Calculate total mass
    # ------------------------------------------------------

    total_mass = sum(masses.values())

    # ------------------------------------------------------
    # Calculate theoretical density
    #
    # ρ = Total Mass / Total Volume
    #
    # This must give the same result as the direct Rule
    # of Mixtures calculation.
    # ------------------------------------------------------

    theoretical_density = total_mass / total_volume

    # ------------------------------------------------------
    # Direct Rule-of-Mixtures density for verification
    # ------------------------------------------------------

    direct_density = composite_density(
        epoxy_density,
        horn_density,
        cotton_density,
        limestone_density,
        epoxy_percent,
        horn_percent,
        cotton_percent,
        limestone_percent,
        total_volume
    )

    # ------------------------------------------------------
    # Return complete result
    # ------------------------------------------------------

    return {
        "volumes": volumes,
        "masses": masses,
        "total_volume": total_volume,
        "total_mass": total_mass,
        "theoretical_density": theoretical_density,
        "direct_rule_of_mixtures_density": direct_density
    }


# ==========================================================
# CALCULATE WEIGHT FRACTIONS
# ==========================================================

def weight_fractions(
    epoxy_percent,
    horn_percent,
    cotton_percent,
    limestone_percent
):
    """
    Converts supplied percentages into decimal fractions.

    IMPORTANT:
    If the input percentages represent volume percentages,
    these are volume fractions and should not be interpreted
    as mass fractions.
    """

    return {
        "Epoxy": float(epoxy_percent) / 100.0,

        "Cow Horn": float(horn_percent) / 100.0,

        "Cotton": float(cotton_percent) / 100.0,

        "Limestone": float(limestone_percent) / 100.0
    }


# ==========================================================
# PERCENTAGE ERROR
# ==========================================================

def percentage_error(experimental, theoretical):
    """
    Calculates percentage difference/error using theoretical
    density as the reference value.

    Formula:

        % Error =
        |Experimental - Theoretical|
        ---------------------------- × 100
              Theoretical
    """

    experimental = float(experimental)
    theoretical = float(theoretical)

    if theoretical == 0:
        raise ValueError(
            "Theoretical value cannot be zero."
        )

    return (
        abs(experimental - theoretical)
        / abs(theoretical)
    ) * 100.0


# ==========================================================
# PREDICTION ACCURACY
# ==========================================================

def prediction_accuracy(error):
    """
    Calculates prediction accuracy.

    Accuracy = 100 - percentage error
    """

    error = float(error)

    accuracy = 100.0 - error

    # Prevent negative accuracy values
    if accuracy < 0:
        accuracy = 0.0

    return accuracy


# ==========================================================
# PENETRATION RESISTANCE INDEX
# ==========================================================

def penetration_index(force, penetration_depth):
    """
    Calculates penetration resistance index.

    Formula:

        PRI = Force / Penetration Depth
    """

    force = float(force)
    penetration_depth = float(penetration_depth)

    if penetration_depth == 0:
        raise ValueError(
            "Penetration depth cannot be zero."
        )

    return force / penetration_depth


# ==========================================================
# FIND OPTIMUM SAMPLE
# ==========================================================

def optimum_sample(samples):
    """
    Finds the sample having the minimum penetration depth.

    Expected format:

        [
            ("F1", penetration_depth),
            ("F2", penetration_depth),
            ...
        ]
    """

    if not samples:
        return None

    return min(
        samples,
        key=lambda x: float(x[1])
    )


# ==========================================================
# END OF FILE
# ==========================================================

