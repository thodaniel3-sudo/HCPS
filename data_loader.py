"""
===========================================================
data_loader.py

Hybrid Composite Prediction System (HCPS)

Experimental Dataset Loader

Loads the HCPS experimental dataset and prepares
the experimentally measured properties for AI training.

Author: Daniel Thomas
===========================================================
"""

import os
import sys
import pandas as pd
import numpy as np


# =========================================================
# GET DATA DIRECTORY
# =========================================================

def get_data_directory():

    if getattr(sys, "frozen", False):

        return sys._MEIPASS

    return os.path.dirname(
        os.path.abspath(__file__)
    )


# =========================================================
# LOAD DATASET
# =========================================================

def load_dataset():

    data_directory = get_data_directory()

    file_name = os.path.join(
        data_directory,
        "HCPS_dataset.csv"
    )

    if not os.path.exists(file_name):

        raise FileNotFoundError(

            "HCPS_dataset.csv was not found.\n\n"
            f"Expected location:\n{file_name}"

        )

    data = pd.read_csv(file_name)

    # Remove accidental spaces from headers
    data.columns = data.columns.str.strip()

    return data


# =========================================================
# PREPARE TRAINING DATA
# =========================================================

def prepare_training_data():

    data = load_dataset()


    # =====================================================
    # INPUT FEATURES
    # =====================================================

    input_columns = [

        "Epoxy (%)",

        "Cow Horn (%)",

        "Cotton Wool (%)",

        "Limestone (%)"

    ]


    # =====================================================
    # EXPERIMENTALLY MEASURED OUTPUTS
    # =====================================================

    output_columns = [

        "Density (g/cm3)",

        "Flexural Strength (MPa)",

        "Compressive Strength (MPa)",

        "Impact Strength (kJ/m2)"

        "Flexural Modulus (GPa)",

    ]


    # =====================================================
    # CHECK INPUT COLUMNS
    # =====================================================

    missing_inputs = [

        column

        for column in input_columns

        if column not in data.columns

    ]


    if missing_inputs:

        raise ValueError(

            "The following input columns are missing "
            "from HCPS_dataset.csv:\n\n"

            + "\n".join(missing_inputs)

            + "\n\nAvailable columns are:\n\n"

            + "\n".join(data.columns)

        )


    # =====================================================
    # CHECK OUTPUT COLUMNS
    # =====================================================

    missing_outputs = [

        column

        for column in output_columns

        if column not in data.columns

    ]


    if missing_outputs:

        raise ValueError(

            "The following experimental output columns "
            "are missing from HCPS_dataset.csv:\n\n"

            + "\n".join(missing_outputs)

            + "\n\nAvailable columns are:\n\n"

            + "\n".join(data.columns)

        )


    # =====================================================
    # CONVERT TO NUMERIC
    # =====================================================

    for column in input_columns:

        data[column] = pd.to_numeric(

            data[column],

            errors="coerce"

        )


    for column in output_columns:

        data[column] = pd.to_numeric(

            data[column],

            errors="coerce"

        )


    # =====================================================
    # KEEP ONLY VALID TRAINING ROWS
    # =====================================================

    training_columns = (

        input_columns

        + output_columns

    )


    data = data.dropna(

        subset=training_columns

    )


    # =====================================================
    # CHECK DATA
    # =====================================================

    if data.empty:

        raise ValueError(

            "HCPS_dataset.csv contains no valid "
            "experimental training data."

        )


    X = data[input_columns].to_numpy(

        dtype=float

    )


    y = data[output_columns].to_numpy(

        dtype=float

    )


    # =====================================================
    # CHECK NUMERICAL VALUES
    # =====================================================

    if not np.isfinite(X).all():

        raise ValueError(

            "Invalid numerical values were found "
            "in the input composition data."

        )


    if not np.isfinite(y).all():

        raise ValueError(

            "Invalid numerical values were found "
            "in the experimental output data."

        )


    # =====================================================
    # CHECK SAMPLE COUNT
    # =====================================================

    if X.shape[0] < 2:

        raise ValueError(

            "At least two valid experimental samples "
            "are required for AI training."

        )


    return X, y


# =========================================================
# TEST LOADER
# =========================================================

if __name__ == "__main__":

    try:

        X, y = prepare_training_data()


        print(
            "\nHCPS DATA LOADER"
        )

        print(
            "=============================="
        )


        print(
            "\nTraining samples:"
        )

        print(
            X.shape[0]
        )


        print(
            "\nInput shape:"
        )

        print(
            X.shape
        )


        print(
            "\nOutput shape:"
        )

        print(
            y.shape
        )


        print(
            "\nInput features:"
        )

        print(
            "1. Epoxy (%)"
        )

        print(
            "2. Cow Horn (%)"
        )

        print(
            "3. Cotton Wool (%)"
        )

        print(
            "4. Limestone (%)"
        )


        print(
            "\nAI target properties:"
        )

        print(
            "1. Density"
        )

        print(
            "2. Flexural Strength"
        )

        print(
            "3. Compressive Strength"
        )

        print(
            "4. Impact Strength"
        )


        print(
            "\nHCPS DATA LOADER STATUS: READY"
        )


    except Exception as e:

        print(
            "\nHCPS DATA LOADER ERROR:"
        )

        print(e)