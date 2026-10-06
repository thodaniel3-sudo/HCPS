"""
===========================================================
HCPS AI Performance Report Module
===========================================================
"""

from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
import numpy as np


def generate_ai_report(model, X, y):

    predictions = model.predict(X)


    r2 = r2_score(
        y,
        predictions
    )


    mae = mean_absolute_error(
        y,
        predictions
    )


    rmse = np.sqrt(
        mean_squared_error(
            y,
            predictions
        )
    )


    report = {

        "Algorithm":
            "Random Forest Multi-Output Regression",

        "Training Samples":
            len(X),

        "Output Properties":
            y.shape[1],

        "R2 Score":
            round(r2,3),

        "MAE":
            round(mae,3),

        "RMSE":
            round(rmse,3),

        "Status":
            "AI Model Ready"

    }


    return report