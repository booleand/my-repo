import pathlib

PACKAGE_ROOT = pathlib.Path(__file__).resolve().parent
TRAINED_MODEL_DIR = PACKAGE_ROOT / "trained_models"
DATASET_DIR = PACKAGE_ROOT / "datasets"

TESTING_DATA_FILE = DATASET_DIR / "test_csv"
TRAINING_DATA_FILE = DATASET_DIR / "trainging.csv"
TARGET = "SalePrice"

FEATURES = [
    "MSSubclass",
    "MSZoning",
    "Neighborhood",
    "OverallQual",
    "OverallCond",
    "YearRemoAdd",
    "RoofStyle",
    "MasVnrType",
    "BsmtQual",
    "BsmtExposure",
    "HeatingQC",
    "CentralAir",
    "1stFlrSF",
    "GrLivArea",
    "BsmtFullBath",
    "KitchenQual",
    "Fireplaces",
    "FireplaceQu",
    "GarageType",
    "GarageFinish",
    "GarageCars",
    "PavedDrive",
    "LotFrontage",
    # this variable is only to calculate temporal variable:
    "YrSold",
]


def save_pipeline() -> None:
    """ Persist the pipeline."""

    pass


def run_training() -> None:
    """ Train the model."""

    print("Training...")


if __name__ == "__main__":
    run_training()
