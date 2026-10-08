from sklearn.pipeline import Pipeline
from sklearn.dummy import DummyRegressor
from sklearn.linear_model import LinearRegression, Ridge, Lasso
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor

from src.features.preprocessing import (
    create_linear_preprocessor,
    create_tree_preprocessor
)


def create_dummy_pipeline():
    # Create naive baseline model
    return Pipeline([
        ("preprocessor", create_linear_preprocessor()),
        ("model", DummyRegressor(strategy="mean"))
    ])


def create_linear_pipeline():
    # Create Linear Regression model
    return Pipeline([
        ("preprocessor", create_linear_preprocessor()),
        ("model", LinearRegression())
    ])


def create_ridge_pipeline(alpha=1.0):
    # Create Ridge Regression model
    return Pipeline([
        ("preprocessor", create_linear_preprocessor()),
        ("model", Ridge(alpha=alpha))
    ])


def create_lasso_pipeline(alpha=0.01):
    # Create Lasso Regression model
    return Pipeline([
        ("preprocessor", create_linear_preprocessor()),
        ("model", Lasso(
            alpha=alpha,
            max_iter=10000
        ))
    ])


def create_decision_tree_pipeline(max_depth=4, random_state=42):
    # Create Decision Tree model
    return Pipeline([
        ("preprocessor", create_tree_preprocessor()),
        ("model", DecisionTreeRegressor(
            max_depth=max_depth,
            random_state=random_state
        ))
    ])


def create_random_forest_pipeline(
    n_estimators=200,
    random_state=42,
    n_jobs=-1
):
    # Create Random Forest model
    return Pipeline([
        ("preprocessor", create_tree_preprocessor()),
        ("model", RandomForestRegressor(
            n_estimators=n_estimators,
            random_state=random_state,
            n_jobs=n_jobs
        ))
    ])