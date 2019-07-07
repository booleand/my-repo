from sklearn.pipeline import Pipeline

import preprocessors as pp

CATEGORICAL_VARS = [
    "MSZoning",
    "Neighbourhood",
    "RoofStyle",
    "MasVnrType",
    "BsmtQual",
    "BsmtExposure",
    "HeatingQC",
    "CentralAir",
    "KitchenQual",
    "FireplaceQu",
    "GarageType",
    "GarageFinish",
    "PavedDrive",
]

PIPELINE_NAME = "lasso_regression"

price_pipe = Pipeline(
    [("categorical_imputer", pp.CategorialImputer(variables=CATEGORICAL_VARS))]
)
