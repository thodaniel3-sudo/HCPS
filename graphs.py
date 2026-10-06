
"""
===========================================================
graphs.py

Hybrid Composite Prediction System (HCPS)

Advanced Graph Visualization Module

Author: Daniel Thomas
===========================================================
"""

import matplotlib.pyplot as plt


# =========================================================
# 1. DENSITY BAR CHART
# =========================================================

def density_bar_chart(density):

    plt.figure(figsize=(7, 5))

    plt.bar(
        ["Composite"],
        [density]
    )

    plt.xlabel(
        "Material"
    )

    plt.ylabel(
        "Density (g/cm³)"
    )

    plt.title(
        "Theoretical Composite Density"
    )

    plt.grid(
        True,
        axis="y"
    )

    plt.tight_layout()

    plt.show()


# =========================================================
# 2. COMPOSITION PIE CHART
# =========================================================

def composition_pie_chart(
        epoxy,
        horn,
        cotton,
        limestone
):

    labels = [
        "Epoxy",
        "Cow Horn",
        "Cotton Wool",
        "Limestone"
    ]

    values = [
        float(epoxy),
        float(horn),
        float(cotton),
        float(limestone)
    ]

    plt.figure(figsize=(7, 7))

    plt.pie(
        values,
        labels=labels,
        autopct="%1.1f%%",
        startangle=90
    )

    plt.title(
        "Hybrid Composite Composition"
    )

    plt.tight_layout()

    plt.show()


# =========================================================
# 3. PROPERTY BAR CHART
# =========================================================

def property_bar_chart(predictions):

    if not predictions:

        raise ValueError(
            "No prediction data is available for plotting."
        )

    # -----------------------------------------------------
    # Use ONLY the properties actually returned by the AI
    # model.
    # -----------------------------------------------------

    names = list(predictions.keys())

    values = [
        float(value)
        for value in predictions.values()
    ]

    plt.figure(figsize=(12, 6))

    plt.bar(
        names,
        values
    )

    plt.xlabel(
        "Engineering Properties"
    )

    plt.ylabel(
        "Predicted Value"
    )

    plt.title(
        "Predicted Composite Engineering Properties"
    )

    plt.xticks(
        rotation=45,
        ha="right"
    )

    plt.grid(
        True,
        axis="y"
    )

    plt.tight_layout()

    plt.show()


# =========================================================
# 4. PROPERTY LINE GRAPH
# =========================================================

def property_line_graph(predictions):

    if not predictions:

        raise ValueError(
            "No prediction data is available for plotting."
        )

    # -----------------------------------------------------
    # IMPORTANT:
    #
    # Do NOT create a separate hard-coded list of
    # properties.
    #
    # We take both X and Y directly from the predictions
    # dictionary.
    #
    # This guarantees that X and Y have the SAME length.
    # -----------------------------------------------------

    properties = list(
        predictions.keys()
    )

    values = [
        float(value)
        for value in predictions.values()
    ]

    # -----------------------------------------------------
    # SAFETY CHECK
    # -----------------------------------------------------

    if len(properties) != len(values):

        raise ValueError(
            "Graph data error: X and Y values "
            "must have the same number of elements."
        )

    # -----------------------------------------------------
    # CREATE GRAPH
    # -----------------------------------------------------

    x = range(
        len(properties)
    )

    plt.figure(figsize=(12, 6))

    plt.plot(
        x,
        values,
        marker="o",
        linewidth=2
    )

    plt.xlabel(
        "Engineering Properties"
    )

    plt.ylabel(
        "Predicted Value"
    )

    plt.title(
        "Predicted Composite Engineering Properties"
    )

    # -----------------------------------------------------
    # Put the actual property names on the X-axis
    # -----------------------------------------------------

    plt.xticks(
        list(x),
        properties,
        rotation=45,
        ha="right"
    )

    plt.grid(
        True,
        axis="y"
    )

    plt.tight_layout()

    plt.show()


# =========================================================
# 5. COMPLETE GRAPH CONTROLLER
# =========================================================

def plot_graph(
        density,
        epoxy,
        horn,
        cotton,
        limestone,
        predictions
):

    # -----------------------------------------------------
    # CHECK PREDICTION DATA
    # -----------------------------------------------------

    if predictions is None:

        raise ValueError(
            "No prediction data is available. "
            "Please run the AI prediction first."
        )

    if not isinstance(predictions, dict):

        raise ValueError(
            "Prediction data must be provided as a dictionary."
        )

    if len(predictions) == 0:

        raise ValueError(
            "Prediction dictionary is empty."
        )

    # -----------------------------------------------------
    # GRAPH 1
    # -----------------------------------------------------

    density_bar_chart(
        density
    )

    # -----------------------------------------------------
    # GRAPH 2
    # -----------------------------------------------------

    composition_pie_chart(
        epoxy,
        horn,
        cotton,
        limestone
    )

    # -----------------------------------------------------
    # GRAPH 3
    # -----------------------------------------------------

    property_bar_chart(
        predictions
    )

    # -----------------------------------------------------
    # GRAPH 4
    # -----------------------------------------------------

    property_line_graph(
        predictions
    )


# =========================================================
# END OF FILE
# =========================================================

