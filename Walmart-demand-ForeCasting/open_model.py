import joblib

# load model
model = joblib.load("linear_regression_walmart_lr.joblib")

print("✅ Model loaded successfully")
print(model)
print("Coefficients:", model.coef_)
print("Intercept:", model.intercept_)