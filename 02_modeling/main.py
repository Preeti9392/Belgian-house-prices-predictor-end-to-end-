# ===============================
# House Price Prediction with CatBoost
# ===============================

# --- Imports ---
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from catboost import CatBoostRegressor, Pool
from sklearn.metrics import (
    mean_absolute_percentage_error,
    mean_squared_error,
    r2_score,
    mean_absolute_error
)
import warnings
from scipy import stats
from joblib import dump
import pickle

# Ignore warnings for cleaner output
warnings.filterwarnings('ignore')

# ===============================
# Load and Inspect Dataset
# ===============================
df = pd.read_csv("data/cleaned_data_before_imputation.csv")
df.info()

# Define feature groups
numeric_columns = ["bedroomCount", "toilet_and_bath", "habitableSurface",
                   "facedeCount", "hasTerrace", "totalParkingCount"]
categorical_columns = ["type", "subtype", "province", "locality",
                       "postCode", "buildingCondition", "epcScore"]

# Ensure categorical columns are strings
for col in categorical_columns:
    df[col] = df[col].astype(str)

# Separate features and target
X = df[numeric_columns + categorical_columns]
y = df["price"]
X.info()

# Split dataset into train/test
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.01, random_state=1234
)

# ===============================
# CatBoost Model (Optimized)
# ===============================
train_pool = Pool(X_train, y_train, cat_features=categorical_columns)
val_pool = Pool(X_test, y_test, cat_features=categorical_columns)

catboost_model = CatBoostRegressor(
    iterations=800,
    learning_rate=0.17,
    depth=5,
    loss_function='RMSE',
    eval_metric='MAE',
    early_stopping_rounds=50,
    verbose=100,
    random_state=42
)

# Train with early stopping
catboost_model.fit(train_pool, eval_set=val_pool)

# ===============================
# Predictions
# ===============================
train_preds = catboost_model.predict(X_train)
test_preds = catboost_model.predict(X_test)

# ===============================
# Evaluation
# ===============================
print("\n📊 Final Evaluation Metrics (CatBoost with RMSE + Early Stopping)")
print("MSE (test):", mean_squared_error(y_test, test_preds))
print("R² (train):", r2_score(y_train, train_preds))
print("R² (test):", r2_score(y_test, test_preds))
print("MAE (train):", mean_absolute_error(y_train, train_preds))
print("MAE (test):", mean_absolute_error(y_test, test_preds))
print("MAPE (train):", mean_absolute_percentage_error(y_train, train_preds))
print("MAPE (test):", mean_absolute_percentage_error(y_test, test_preds))

# ===============================
# Save Model (Joblib & Pickle)
# ===============================
dump(catboost_model, 'model/catboost_price_prediction_model.joblib')

with open('model/catboost_price_prediction_model.pkl', 'wb') as f:
    pickle.dump(catboost_model, f)

# ===============================
# Visualizations
# ===============================

# Actual vs Predicted Scatter Plot
plt.figure(figsize=(8, 6))
plt.scatter(y_test, test_preds, alpha=0.4, color='royalblue')
plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], 'r--', lw=2)
plt.xlabel("Actual Price (€)")
plt.ylabel("Predicted Price (€)")
plt.title("CatBoost: Actual vs Predicted Prices")
plt.grid(True)
plt.tight_layout()
plt.show() 

# Q-Q Plot of Residuals
residuals = y_test - test_preds
plt.figure(figsize=(8, 6))
stats.probplot(residuals, dist="norm", plot=plt)
plt.title("Q-Q Plot of Residuals (CatBoost)", fontsize=14)
plt.xlabel("Theoretical Quantiles", fontsize=12)
plt.ylabel("Sample Quantiles", fontsize=12)
plt.grid(True, linestyle='--', alpha=0.6)
plt.tight_layout()
plt.show()
