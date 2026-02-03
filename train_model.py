import joblib
import numpy as np
from sklearn.linear_model import LogisticRegression

# Toy dataset (3 features)
X = np.array([
    [1.0, 2.0, 3.0],
    [1.0, 1.0, 1.0],
    [2.0, 1.0, 0.5],
    [3.0, 3.0, 3.0],
    [0.5, 1.0, 2.0],
    [2.5, 2.0, 1.0],
])

y = np.array([1, 0, 0, 1, 0, 1])

model = LogisticRegression()
model.fit(X, y)

joblib.dump(model, "model.pkl")
print("✅ model.pkl created successfully")
