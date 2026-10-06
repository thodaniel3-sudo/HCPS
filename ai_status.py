"""
===========================================================
ai_status.py

HCPS AI Monitoring Module

Displays information about the trained AI model
and verifies the experimental training dataset.

Author: Daniel Thomas
===========================================================
"""

import numpy as np
from sklearn.metrics import r2_score

from dataset_loader import (
    prepare_training_data,
    load_dataset,
    INPUT_COLUMNS,
    TARGET_COLUMNS
)


# ==========================================================
# GET AI MODEL STATUS
# ==========================================================

def get_ai_status(model):
    """
    Generate a status report for the HCPS AI model.

    Parameters
    ----------
    model : HCPS_AI
        Trained HCPS AI model.

    Returns
    -------
    dict
        AI model status information.
    """

    # ------------------------------------------------------
    # Check that the AI model exists
    # ------------------------------------------------------

    if model is None:

        raise ValueError(
            "HCPS AI model is not available."
        )


    # ------------------------------------------------------
    # Check that the model has been trained
    # ------------------------------------------------------

    if not model.is_trained():

        raise ValueError(
            "HCPS AI model has not been trained."
        )


    # ======================================================
    # LOAD TRAINING DATA
    # ======================================================

    X, y = prepare_training_data()


    # ======================================================
    # VERIFY INPUT FEATURES
    # ======================================================

    if list(X.columns) != INPUT_COLUMNS:

        raise ValueError(
            "The AI input features in the training data "
            "do not match the HCPS AI configuration."
        )


    # ======================================================
    # VERIFY TARGET PROPERTIES
    # ======================================================

    if list(y.columns) != TARGET_COLUMNS:

        raise ValueError(
            "The experimental output properties in "
            "HCPS_dataset.csv do not match the HCPS AI "
            "configuration.\n\n"
            "Expected:\n"
            +
            "\n".join(
                f"- {column}"
                for column in TARGET_COLUMNS
            )
            +
            "\n\nFound:\n"
            +
            "\n".join(
                f"- {column}"
                for column in y.columns
            )
        )


    # ======================================================
    # VERIFY MODEL TARGET CONFIGURATION
    # ======================================================

    model_target_names = model.get_target_names()

    if list(model_target_names) != TARGET_COLUMNS:

        raise ValueError(
            "The AI model target configuration does not "
            "match the experimental dataset.\n\n"
            "Dataset targets:\n"
            +
            "\n".join(
                f"- {column}"
                for column in TARGET_COLUMNS
            )
            +
            "\n\nAI model targets:\n"
            +
            "\n".join(
                f"- {column}"
                for column in model_target_names
            )
        )


    # ======================================================
    # GENERATE TRAINING PREDICTIONS
    # ======================================================

    try:

        prediction = model.model.predict(X)

    except Exception as error:

        raise ValueError(
            "The HCPS AI model could not generate "
            f"training predictions.\n\nDetails: {error}"
        )


    # ======================================================
    # CHECK PREDICTION SHAPE
    # ======================================================

    if prediction.ndim != 2:

        raise ValueError(
            "The AI model returned an invalid prediction "
            "format."
        )


    if prediction.shape[1] != len(TARGET_COLUMNS):

        raise ValueError(
            "The number of AI prediction outputs does "
            "not match the number of experimental "
            "target properties."
        )


    # ======================================================
    # CHECK NUMERICAL VALUES
    # ======================================================

    if not np.isfinite(prediction).all():

        raise ValueError(
            "The AI model produced invalid numerical "
            "prediction values."
        )


    # ======================================================
    # CALCULATE R²
    # ======================================================

    try:

        score = r2_score(
            y,
            prediction,
            multioutput="uniform_average"
        )

    except Exception as error:

        raise ValueError(
            "Unable to calculate the AI model R² score.\n\n"
            f"Details: {error}"
        )


    # ======================================================
    # DETERMINE STATUS
    # ======================================================

    if score >= 0.90:

        model_status = "READY"

    else:

        model_status = "REQUIRES MORE DATA"


    # ======================================================
    # CREATE STATUS REPORT
    # ======================================================

    status = {

        "Model":
        "Random Forest Multi Output",

        "Training Samples":
        len(X),

        "Input Variables":
        len(INPUT_COLUMNS),

        "Output Properties":
        len(TARGET_COLUMNS),

        "R2 Accuracy":
        round(float(score), 3),

        "Status":
        model_status

    }


    return status


# ==========================================================
# END OF FILE
# ==========================================================