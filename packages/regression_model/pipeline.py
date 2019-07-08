from sklean.linear_model import Lasso
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import MinMaxScaler

import preprocessors as pp


# categorical variables with NA in train set
CATEGORICAL_VARS_WITH_NA = [
    "MasVnrType",
    "BsmtQual",
    "BsmtExposure",
    "FireplaceQu",
    "GarageType",
    "GarageFinish",
]

TEMPORAL_VARS = "YearRemodAdd"

# this variable is to calculate the temporal variable,
# can be dropped afterwards
DROP_FEATURES = "YrsSold"

# variables to log transform

NUMERICAL_LOG_VARS = ["LotFrontge", "1stFlrSF", "GrLivArea"]

# numerical variables with NA in train set
NUMERICAL_VARS_WITH_NA = ["LotFrontage"]

# categorical variables to encode
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


price_pipe = Pipeline(
    [
        (
            "categorical_imputer",
            pp.CategorialImputer(variables=CATEGORICAL_VARS_WITH_NA),
        ),
        ("numerical_imputer", pp.NumericalImputer(vairbales=NUMERICAL_VARS_WITH_NA)),
        (
            "temporal_variable",
            pp.TEMPORAL_VARIABLE_ESTIMATOR(
                variables=TEMPORAL_VARS, reference_variable=TEMPORAL_VARS
            ),
        ),
        (
            "rare_label_encoder",
            pp.RareLabelCategoricalEncoder(tol=0.01, variables=CATEGORICAL_VARS),
        ),
        ("categorical_encoder", pp.CategoricalEncoder(variables=NUMERICAL_LOG_VARS)),
        ("log_transformer", pp.LogTransformer(variables=NUMERICAL_LOG_VARS)),
        ("drop_features", pp.DropUnecessaryFeatures(variables_to_drop=DROP_FEATURES)),
        ("scaler", MinMaxScaler()),
        ("Linear_model", Lassor(alpha=0.005, random_state=0)),
    ]
)
