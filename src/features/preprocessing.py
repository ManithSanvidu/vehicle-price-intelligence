from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.impute import SimpleImputer


NUMERIC_FEATURES = [
    "Engine (cc)",
    "Vehicle_Age",
    "Feature_Count"
]


CATEGORICAL_FEATURES = [
    "Brand",
    "Model",
    "Gear",
    "Fuel Type",
    "Town",
    "Leasing",
    "Condition",
    "AIR CONDITION",
    "POWER STEERING",
    "POWER MIRROR",
    "POWER WINDOW",
    "Listing_Month"
]


def create_linear_preprocessor():
    """
    Preprocessing for Linear Regression, Ridge and Lasso.
    """

    numeric_pipeline = Pipeline([
        ("imputer", SimpleImputer(strategy="median")),
        ("scaler", StandardScaler())
    ])

    categorical_pipeline = Pipeline([
        ("encoder", OneHotEncoder(
            handle_unknown="infrequent_if_exist",
            min_frequency=10
        ))
    ])

    preprocessor = ColumnTransformer([
        ("num", numeric_pipeline, NUMERIC_FEATURES),
        ("cat", categorical_pipeline, CATEGORICAL_FEATURES)
    ])

    return preprocessor


def create_tree_preprocessor():
    """
    Preprocessing for tree-based regression models.
    """

    numeric_pipeline = Pipeline([
        ("imputer", SimpleImputer(strategy="median"))
    ])

    categorical_pipeline = Pipeline([
        ("encoder", OneHotEncoder(
            handle_unknown="infrequent_if_exist",
            min_frequency=10
        ))
    ])

    preprocessor = ColumnTransformer([
        ("num", numeric_pipeline, NUMERIC_FEATURES),
        ("cat", categorical_pipeline, CATEGORICAL_FEATURES)
    ])

    return preprocessor