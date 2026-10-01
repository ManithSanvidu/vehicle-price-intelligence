import pandas as pd
from sklearn.model_selection import train_test_split


def clean_vehicle_data(df):
    """
    Apply the agreed data-cleaning steps.
    """

    df_clean = df.copy()

    # Remove exported identifier
    df_clean = df_clean.drop(
        columns=["Unnamed: 0"],
        errors="ignore"
    )

    # Remove rows without the target
    df_clean = df_clean.dropna(
        subset=["Price"]
    )

    # Remove exact duplicate observations
    df_clean = df_clean.drop_duplicates()

    # Convert Date to datetime
    df_clean["Date"] = pd.to_datetime(
        df_clean["Date"],
        errors="coerce"
    )

    return df_clean


def create_shared_split(
    df_clean,
    test_size=0.20,
    random_state=42
):
    """
    Create the shared train/test split.
    """

    X = df_clean.drop(columns=["Price"])
    y = df_clean["Price"]

    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=test_size,
        random_state=random_state
    )

    return X_train, X_test, y_train, y_test
