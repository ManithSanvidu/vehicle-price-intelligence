# Project Decision Log

This log records important project decisions, the reasons for them, and the evidence used.

## Feature Engineering

| Decision | Reason / Evidence |
|---|---|
| Create `Vehicle_Age` | Vehicle age is more directly meaningful for price prediction than raw `YOM`. |
| Create `Listing_Month` | Retains possible seasonal information from the listing date. |
| Create `Feature_Count` | Summarizes the number of available vehicle equipment features. |
| Remove `YOM` | Its information is represented through `Vehicle_Age`. |
| Remove `Mileage(KM)` | It was redundant with `YOM` in the training data. |
| Remove `Date` | Relevant information was retained through `Vehicle_Age` and `Listing_Month`. |

## Initial Modelling

| Decision | Reason / Evidence |
|---|---|
| Use 5-fold cross-validation | Provides a more reliable basis for model comparison using training data only. |
| Use RMSE as the main metric | Larger vehicle-price prediction errors should receive a greater penalty. |
| Use Linear Regression as a predictive baseline | Provides a simple and interpretable starting model for the continuous target. |
| Test Ridge and Lasso | Evaluates whether regularization improves the linear baseline. |
| Select Ridge `alpha=1.0` | Lowest Ridge CV RMSE among the tested alpha values. |
| Select Lasso `alpha=0.01` | Lowest Lasso CV RMSE among the tested alpha values. |
| Test Decision Tree | Checks whether a nonlinear model improves over the linear models. |
| Test Random Forest | Checks whether an ensemble of trees improves over a single tree. |
| Select Random Forest as the strongest initial model | It achieved the lowest CV RMSE of 14.7322 and highest CV R² of 0.8954 among the tested initial configurations. |