## 🏦 Bank Customer Churn Prediction System

This project is a production-ready machine learning system designed to predict customer churn for banking institutions. The goal is to help banks identify customers who are likely to leave, allowing them to take proactive retention measures and reduce revenue loss.

The system uses a supervised learning approach trained on historical customer data, including demographic details, account information, and behavioral features. A full preprocessing and modeling pipeline was built using scikit-learn, ensuring that data transformation (scaling and encoding) is handled automatically and consistently during both training and prediction.

The trained model is deployed through a Flask-based web application, enabling real-time churn predictions via a user interface or API integration. The system outputs both a churn prediction (Yes/No) and a churn probability score, along with a risk classification (Low, Medium, High), making it suitable for business decision-making.

---

## 🔧 Key Features

* End-to-end machine learning pipeline
* Automatic preprocessing using ColumnTransformer
* Random Forest classification model
* Probability-based risk scoring
* Web interface for real-time prediction
* Production-ready Flask backend
* Logging for traceability

---

## 📊 Model Performance

* Accuracy: ~86%
* ROC-AUC: ~0.85

These metrics indicate strong predictive capability and reliable customer risk segmentation.

---

## 💼 Business Impact

This system enables banks to:

* Identify high-risk customers early
* Reduce churn through targeted retention strategies
* Improve customer lifetime value
* Support data-driven decision-making

---

## 🚀 Deployment Architecture

* Model trained in Python using scikit-learn
* Full preprocessing pipeline embedded in model
* Deployed using Flask
* Structured for API-based integration with banking systems

-
