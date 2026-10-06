"""
===========================================================
dataset_loader.py

HCPS Dataset Loader

Loads and validates experimental CSV data for AI training.

Dataset:
HCPS_dataset.csv

AI INPUT FEATURES:
1. Epoxy (%)
2. Cow Horn (%)
3. Cotton Wool (%)
4. Limestone (%)

AI TARGET PROPERTIES:
1. Density (g/cm3)
2. Flexural Strength (MPa)
3. Flexural Modulus (GPa)
4. Compressive Strength (MPa)
5. Impact Strength (kJ/m2)

Author: Daniel Thomas
Project:
Development of an Eco-Friendly Epoxy Hybrid Composite,
Reinforced with Bio-Waste for Automotive Application
===========================================================
"""

import os
import sys
import numpy as np
import pandas as pd


# ==========================================================
# DATASET CONFIGURATION
# ==========================================================

DATASET_FILE = "HCPS_dataset.csv"


# ==========================================================
# AI INPUT FEATURES
# ==========================================================

INPUT_COLUMNS = [
    "Epoxy (%)",
    "Cow Horn (%)",
    "Cotton Wool (%)",
    "Limestone (%)"
]


# ==========================================================
# AI TARGET PROPERTIES
# ==========================================================

TARGET_COLUMNS = [
    "Density (g/cm3)",
    "Flexural Strength (MPa)",
    "Flexural Modulus (GPa)",
    "Compressive Strength (MPa)",
    "Impact Strength (kJ/m2)"
]


# ==========================================================
# DATASET PATH
# ==========================================================

def get_dataset_path():
    """
    Determine the correct location of HCPS_dataset.csv.

    Works both when running:
        1. The normal Python source project
        2. A PyInstaller one-file executable
    """

    # ------------------------------------------------------
    # PyInstaller one-file executable
    # ------------------------------------------------------

    if getattr(sys, "frozen", False) and hasattr(
        sys,
        "_MEIPASS"
    ):

        base_directory = sys._MEIPASS

    # ------------------------------------------------------
    # Normal Python execution
    # ------------------------------------------------------

    else:

        base_directory = os.path.dirname(
            os.path.abspath(__file__)
        )

    return os.path.join(
        base_directory,
        DATASET_FILE
    )


# ==========================================================
# LOAD DATASET
# ==========================================================

def load_dataset():
    """
    Load HCPS_dataset.csv.

    The function supports both normal Python execution
    and PyInstaller packaged execution.

    Returns
    -------
    pandas.DataFrame
        Loaded and cleaned dataset.
    """

    # ------------------------------------------------------
    # Locate dataset
    # ------------------------------------------------------

    file_path = get_dataset_path()

    # ------------------------------------------------------
    # Check that dataset exists
    # ------------------------------------------------------

    if not os.path.isfile(file_path):

        raise FileNotFoundError(
            f"\nHCPS dataset was not found.\n\n"
            f"Expected file:\n{file_path}\n\n"
            f"Please make sure '{DATASET_FILE}' "
            f"is included with the HCPS application."
        )

    # ------------------------------------------------------
    # Read CSV
    # ------------------------------------------------------

    try:

        data = pd.read_csv(file_path)

    except Exception as error:

        raise ValueError(
            f"\nUnable to read {DATASET_FILE}.\n\n"
            f"Details: {error}"
        )

    # ------------------------------------------------------
    # Check that dataset contains data
    # ------------------------------------------------------

    if data.empty:

        raise ValueError(
            f"\n{DATASET_FILE} contains no data rows."
        )

    # ------------------------------------------------------
    # Clean column names
    #
    # Removes:
    # - Leading/trailing spaces
    # - Accidental Markdown **
    # ------------------------------------------------------

    data.columns = (
        data.columns
        .astype(str)
        .str.strip()
        .str.replace(
            "**",
            "",
            regex=False
        )
        .str.strip()
    )

    return data


# ==========================================================
# VALIDATE REQUIRED COLUMNS
# ==========================================================

def validate_dataset_columns(data):
    """
    Verify that the dataset contains all required
    AI input and target columns.

    Parameters
    ----------
    data : pandas.DataFrame
        Dataset to validate.
    """

    required_columns = (
        INPUT_COLUMNS +
        TARGET_COLUMNS
    )

    missing_columns = [
        column
        for column in required_columns
        if column not in data.columns
    ]

    if missing_columns:

        available_columns = "\n".join(
            f"- {column}"
            for column in data.columns
        )

        missing = "\n".join(
            f"- {column}"
            for column in missing_columns
        )

        raise ValueError(
            "\nThe following required columns are "
            "missing from HCPS_dataset.csv:\n\n"
            f"{missing}\n\n"
            "Available columns in the dataset:\n\n"
            f"{available_columns}"
        )


# ==========================================================
# CLEAN NUMERICAL DATA
# ==========================================================

def clean_numeric_data(data):
    """
    Convert all AI input and target columns to numeric
    values and remove invalid rows.

    Parameters
    ----------
    data : pandas.DataFrame
        Dataset to clean.

    Returns
    -------
    pandas.DataFrame
        Cleaned dataset.
    """

    columns_to_clean = (
        INPUT_COLUMNS +
        TARGET_COLUMNS
    )

    cleaned_data = data.copy()

    # ------------------------------------------------------
    # Remove accidental Markdown characters and convert
    # values to numeric
    # ------------------------------------------------------

    for column in columns_to_clean:

        cleaned_data[column] = (
            cleaned_data[column]
            .astype(str)
            .str.replace(
                "**",
                "",
                regex=False
            )
            .str.strip()
        )

        cleaned_data[column] = pd.to_numeric(
            cleaned_data[column],
            errors="coerce"
        )

    # ------------------------------------------------------
    # Remove rows containing missing numerical values
    # ------------------------------------------------------

    cleaned_data = cleaned_data.dropna(
        subset=columns_to_clean
    )

    if cleaned_data.empty:

        raise ValueError(
            "\nNo valid numerical data remains in "
            "HCPS_dataset.csv after cleaning."
        )

    return cleaned_data


# ==========================================================
# VALIDATE COMPOSITION DATA
# ==========================================================

def validate_compositions(X):
    """
    Validate the four composition percentages.

    Requirements:
    - No negative values
    - Total composition must equal 100%

    Parameters
    ----------
    X : pandas.DataFrame
        AI input features.
    """

    # ------------------------------------------------------
    # Check for negative composition values
    # ------------------------------------------------------

    negative_values = (X < 0).any()

    if negative_values.any():

        negative_columns = [
            column
            for column, value
            in negative_values.items()
            if value
        ]

        raise ValueError(
            "\nNegative composition percentages "
            "were found in HCPS_dataset.csv.\n\n"
            "Affected columns:\n"
            +
            "\n".join(
                f"- {column}"
                for column in negative_columns
            )
        )

    # ------------------------------------------------------
    # Calculate total composition
    # ------------------------------------------------------

    composition_total = (
        X["Epoxy (%)"]
        +
        X["Cow Horn (%)"]
        +
        X["Cotton Wool (%)"]
        +
        X["Limestone (%)"]
    )

    # ------------------------------------------------------
    # Allow a very small numerical tolerance
    # ------------------------------------------------------

    invalid_compositions = ~np.isclose(
        composition_total,
        100.0,
        atol=0.001
    )

    if invalid_compositions.any():

        invalid_rows = (
            X.index[
                invalid_compositions
            ]
            .tolist()
        )

        raise ValueError(
            "\nInvalid composition percentages detected "
            "in HCPS_dataset.csv.\n\n"
            f"Problem rows: {invalid_rows}\n\n"
            "Epoxy + Cow Horn + Cotton Wool + "
            "Limestone must equal 100%."
        )


# ==========================================================
# PREPARE TRAINING DATA
# ==========================================================

def prepare_training_data():
    """
    Prepare the HCPS experimental dataset for
    machine-learning training.

    Returns
    -------
    X : pandas.DataFrame
        Four composition input features.

    y : pandas.DataFrame
        Five experimentally measured target properties.
    """

    # ------------------------------------------------------
    # Load dataset
    # ------------------------------------------------------

    data = load_dataset()

    # ------------------------------------------------------
    # Validate required columns
    # ------------------------------------------------------

    validate_dataset_columns(data)

    # ------------------------------------------------------
    # Clean numerical values
    # ------------------------------------------------------

    data = clean_numeric_data(data)

    # ------------------------------------------------------
    # Select AI input features
    # ------------------------------------------------------

    X = data[
        INPUT_COLUMNS
    ].copy()

    # ------------------------------------------------------
    # Select AI target properties
    # ------------------------------------------------------

    y = data[
        TARGET_COLUMNS
    ].copy()

    # ------------------------------------------------------
    # Validate compositions
    # ------------------------------------------------------

    validate_compositions(X)

    # ------------------------------------------------------
    # Verify finite numerical values
    # ------------------------------------------------------

    if not np.isfinite(
        X.to_numpy()
    ).all():

        raise ValueError(
            "\nNon-finite values were detected in "
            "the AI input features."
        )

    if not np.isfinite(
        y.to_numpy()
    ).all():

        raise ValueError(
            "\nNon-finite values were detected in "
            "the AI target properties."
        )

    # ------------------------------------------------------
    # Minimum training sample check
    # ------------------------------------------------------

    if len(X) < 2:

        raise ValueError(
            "\nAt least two valid experimental samples "
            "are required for AI training."
        )

    # ------------------------------------------------------
    # Reset indexes
    # ------------------------------------------------------

    X = X.reset_index(
        drop=True
    )

    y = y.reset_index(
        drop=True
    )

    # ------------------------------------------------------
    # Return training data
    # ------------------------------------------------------

    return X, y


# ==========================================================
# DATASET INFORMATION
# ==========================================================

def get_dataset_information():
    """
    Return basic information about the HCPS dataset.

    Returns
    -------
    dict
        Dataset information.
    """

    data = load_dataset()

    return {
        "dataset_file": DATASET_FILE,
        "sample_count": len(data),
        "input_features": INPUT_COLUMNS.copy(),
        "target_properties": TARGET_COLUMNS.copy(),
        "input_count": len(INPUT_COLUMNS),
        "target_count": len(TARGET_COLUMNS)
    }


# ==========================================================
# END OF FILE
# ==========================================================