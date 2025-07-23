import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.linear_model import LinearRegression, Ridge
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor
from sklearn.neighbors import KNeighborsRegressor
import joblib

# Load dataset
df = pd.read_csv("gpa_data_fake_5000.csv")

X = df[["current_credits", "total_credits", "current_gpa", "target_gpa", "num_2_credit", "num_3_credit"]]
y = df["final_gpa"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

models = {
    "Linear Regression": LinearRegression(),
    "Ridge Regression": Ridge(alpha=1.0),
    "Decision Tree": DecisionTreeRegressor(random_state=42),
    "Random Forest": RandomForestRegressor(n_estimators=100, random_state=42),
    "Gradient Boosting": GradientBoostingRegressor(n_estimators=100, random_state=42),
    "K-Nearest Neighbors": KNeighborsRegressor(n_neighbors=5)
}

best_model = None
best_model_name = ""
best_r2 = float("-inf") 

for name, model in models.items():
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    mse = mean_squared_error(y_test, y_pred)
    r2 = r2_score(y_test, y_pred)

    print(f"📊 {name}")
    print(f"  🔹 MSE: {round(mse, 4)}")
    print(f"  🔹 R²: {round(r2, 4)}\n")

    if r2 > best_r2:
        best_r2 = r2
        best_model = model
        best_model_name = name

# Lưu mô hình tốt nhất
joblib.dump(best_model, "gpa_predictor_model.pkl")
print(f"✅ Best model ({best_model_name}) saved as gpa_predictor_model.pkl with R² = {round(best_r2, 4)}")
