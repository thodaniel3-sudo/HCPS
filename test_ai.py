"""
===========================================================
test_ai.py

HCPS Artificial Intelligence Validation System

Engineering AI Performance Testing

Author: Daniel Thomas
===========================================================
"""

import numpy as np
from sklearn.metrics import (
    r2_score,
    mean_absolute_error,
    mean_squared_error
)

from sklearn.model_selection import cross_val_score


from data_loader import prepare_training_data
from machine_learning import HCPS_AI



# ======================================================
# LOAD DATA
# ======================================================

X, y = prepare_training_data()



print("\nHCPS AI VALIDATION REPORT")
print("=========================")



print("\nDATASET INFORMATION")
print("-------------------")

print(
    "Training Samples:",
    len(X)
)

print(
    "Input Features:",
    X.shape[1]
)

print(
    "Prediction Outputs:",
    y.shape[1]
)



# ======================================================
# TRAIN MODEL
# ======================================================


ai = HCPS_AI()


ai.train(
    X,
    y
)



print("\nAI MODEL STATUS")
print("----------------")

print(
    "Trained:",
    ai.is_trained()
)



# ======================================================
# MODEL PREDICTION
# ======================================================


prediction = ai.predict(
    X[0]
)


print("\nTEST SAMPLE PREDICTION")
print("----------------------")


properties = [

"Density (g/cm³)",
"Tensile Strength (MPa)",
"Flexural Strength (MPa)",
"Compressive Strength (MPa)",
"Young Modulus (GPa)",
"Hardness (Shore D)",
"Impact Strength (kJ/m²)",
"Penetration Depth (mm)"

]


for name,value in zip(properties,prediction):

    print(
        f"{name}: {value:.3f}"
    )



# ======================================================
# PERFORMANCE
# ======================================================


all_predictions = ai.model.predict(X)



r2 = r2_score(
    y,
    all_predictions
)


mae = mean_absolute_error(
    y,
    all_predictions
)


rmse = np.sqrt(
    mean_squared_error(
        y,
        all_predictions
    )
)



print("\nMODEL PERFORMANCE")
print("-----------------")


print(
    f"R² Score: {r2:.3f}"
)


print(
    f"MAE: {mae:.3f}"
)


print(
    f"RMSE: {rmse:.3f}"
)



# ======================================================
# FEATURE IMPORTANCE
# ======================================================


print("\nFEATURE IMPORTANCE")
print("------------------")


features = [

"Epoxy (%)",
"Cow-Horn (%)",
"Cotton (%)",
"Limestone (%)"

]


importance = np.mean(

    [

        estimator.feature_importances_

        for estimator in ai.model.estimators_

    ],

    axis=0

)



for feature,value in zip(
    features,
    importance
):

    print(
        f"{feature}: {value:.3f}"
    )



# ======================================================
# FINAL AI CHECK
# ======================================================


print("\nHCPS AI READINESS")
print("=================")


if r2 >= 0.90:

    print(
        "STATUS: AI MODEL READY FOR ENGINEERING PREDICTION"
    )

else:

    print(
        "STATUS: MORE DATA REQUIRED"
    )