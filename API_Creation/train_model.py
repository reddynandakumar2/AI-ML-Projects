import pandas as pd
from sklearn.linear_model import LinearRegression
import joblib

# Sample data
data = {
    "experience": [1, 2, 3, 4, 5, 6, 7],
    "salary": [30000, 40000, 50000, 60000, 70000, 80000, 90000]
}

df = pd.DataFrame(data)

X = df[["experience"]]
y = df["salary"]

# Train model
model = LinearRegression()
model.fit(X, y)

# Save model
joblib.dump(model, "salary_model.pkl")

print("Model Saved!")