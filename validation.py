# ==========================================================
# HYBRID COMPOSITE PREDICTION SYSTEM (HCPS)
# validation.py
#
# Input Validation Module
#
# Project:
# Development of a Sustainable Hybrid Composite
# for Penetration Resistance Application
# ==========================================================


def is_empty(values):
    """
    Checks whether any input field is empty.

    Returns:
        True  -> if any field is empty
        False -> if all fields contain data
    """

    for value in values:
        if str(value).strip() == "":
            return True

    return False


def is_positive_number(value):
    """
    Checks if a value is a positive number.
    """

    try:
        number = float(value)

        if number <= 0:
            return False

        return True

    except ValueError:
        return False


def validate_numbers(values):
    """
    Ensures every supplied value is a positive number.

    Returns:
        (True, "")
        (False, error_message)
    """

    for index, value in enumerate(values):

        if not is_positive_number(value):

            return (
                False,
                f"Invalid value entered in Field {index + 1}.\n"
                "Please enter positive numerical values only."
            )

    return True, ""


def validate_percentages(
    epoxy,
    horn,
    cotton,
    limestone
):
    """
    Checks that reinforcement percentages total 100%.
    """

    total = (
        epoxy +
        horn +
        cotton +
        limestone
    )

    if abs(total - 100) > 0.001:

        return (
            False,
            f"Total composition is {total:.2f}%.\n"
            "The total percentage must equal exactly 100%."
        )

    return True, ""


def validate_all(
    epoxy_density,
    horn_density,
    cotton_density,
    limestone_density,
    epoxy_percent,
    horn_percent,
    cotton_percent,
    limestone_percent
):
    """
    Performs all validation checks.
    """

    values = [

        epoxy_density,
        horn_density,
        cotton_density,
        limestone_density,

        epoxy_percent,
        horn_percent,
        cotton_percent,
        limestone_percent

    ]

    # Empty fields

    if is_empty(values):

        return (
            False,
            "Please fill in all input fields."
        )

    # Numeric values

    valid, message = validate_numbers(values)

    if not valid:

        return (
            False,
            message
        )

    # Percentage check

    valid, message = validate_percentages(

        float(epoxy_percent),
        float(horn_percent),
        float(cotton_percent),
        float(limestone_percent)

    )

    if not valid:

        return (
            False,
            message
        )

    return (
        True,
        "Validation Successful"
    )


# ==========================================================
# END OF FILE
# ==========================================================