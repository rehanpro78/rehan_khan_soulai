# California Housing Price Prediction

This project builds and deploys a machine learning model to predict house prices using the California Housing dataset.

## Project Overview

- **Data Preprocessing:** EDA, feature scaling, and feature engineering.
- **Model Training:** Baseline and tuned RandomForestRegressor.
- **Model Persistence:** Saved tuned model using Joblib.
- **Deployment:** Flask API serving predictions.

## Files

- `notebook.ipynb` - Jupyter Notebook with all steps.
- `app.py` - Flask application to serve predictions.
- `requirements.txt` - List of Python packages.
- `tuned_rf_model.joblib` - Trained model file.

## How to Run Locally

1. Clone the repository:
   ```bash
   git clone https://github.com/<your-username>/california-housing-price-prediction.git
   cd california-housing-price-prediction
