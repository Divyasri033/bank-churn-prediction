import pandas as pd
from flask import Flask, render_template, request
import joblib
import logging

app = Flask(__name__)

# Logging (important for production)
logging.basicConfig(level=logging.INFO)

# Load full pipeline (NOT old model.pkl)
model = joblib.load("model/bank_churn_pipeline.pkl")


@app.route("/", methods=["GET", "POST"])
def home():
    prediction = None
    probability = None
    risk_level = None

    if request.method == "POST":
        try:
            # Collect raw input (no manual encoding)
            input_data = {
                "credit_score": float(request.form["credit_score"]),
                "country": request.form["country"],
                "gender": request.form["gender"],
                "age": float(request.form["age"]),
                "tenure": float(request.form["tenure"]),
                "balance": float(request.form["balance"]),
                "products_number": float(request.form["products_number"]),
                "credit_card": int(request.form["credit_card"]),
                "active_member": int(request.form["active_member"]),
                "estimated_salary": float(request.form["estimated_salary"]),
            }

            input_df = pd.DataFrame([input_data])

            # Predict
            result = model.predict(input_df)[0]
            prob = model.predict_proba(input_df)[0][1]

            probability = round(prob * 100, 2)

            # Custom business threshold logic
            if probability < 40:
                risk_level = "Low"
            elif probability < 70:
                risk_level = "Medium"
            else:
                risk_level = "High"

            prediction = (
                "Customer Will Churn"
                if result == 1
                else "Customer Will Not Churn"
            )

            logging.info(f"Prediction: {prediction}, Probability: {probability}%")

        except Exception as e:
            logging.error(str(e))
            prediction = "Invalid Input Data"
            probability = None
            risk_level = None

    return render_template(
        "index.html",
        prediction=prediction,
        probability=probability,
        risk_level=risk_level,
    )


if __name__ == "__main__":
    app.run(debug=False)  # Turn OFF debug for production
