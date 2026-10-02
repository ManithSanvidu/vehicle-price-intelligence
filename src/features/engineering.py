def engineer_vehicle_features(X):
    X = X.copy()

    # Vehicle age at the time of listing
    X["Vehicle_Age"] = X["Date"].dt.year - X["YOM"]

    # Month the vehicle was listed
    X["Listing_Month"] = X["Date"].dt.month

    # Count available vehicle features
    feature_cols = [
        "AIR CONDITION",
        "POWER STEERING",
        "POWER MIRROR",
        "POWER WINDOW"
    ]

    X["Feature_Count"] = (
        X[feature_cols] == "Available"
    ).sum(axis=1)

    # Remove redundant/raw columns
    X = X.drop(
        columns=["YOM", "Mileage(KM)", "Date"]
    )

    return X