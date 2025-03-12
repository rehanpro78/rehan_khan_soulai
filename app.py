from flask import Flask, request, jsonify, render_template
import joblib
import numpy as np
import pandas as pd

app = Flask(__name__)

# Global variable for lazy loading the model
model = None

def load_model():
    global model
    if model is None:
        # Load the model using memory mapping to reduce peak memory usage
        model = joblib.load("tuned_rf_model.joblib", mmap_mode='r')
    return model

# Landing page endpoint: renders the main index page with project details.
@app.route('/')
def index():
    return render_template("index.html")

# API endpoint: accepts JSON input and returns the predicted price.
@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.get_json()
        feature_order = ["MedInc", "HouseAge", "AveRooms", "AveBedrms",
                         "Population", "AveOccup", "Latitude", "Longitude"]
        features = [data.get(feature) for feature in feature_order]
        # Convert to DataFrame with proper column names to avoid warnings.
        features_df = pd.DataFrame([features], columns=feature_order)
        m = load_model()  # Lazy load the model
        prediction_log = m.predict(features_df)
        prediction = np.expm1(prediction_log[0])  # Inverse log1p transformation
        return jsonify({'predicted_price': prediction})
    except Exception as e:
        return jsonify({'error': str(e)})

# Interactive UI endpoint: allows users to input data via a form.
@app.route('/predictui', methods=['GET', 'POST'])
def predict_ui():
    if request.method == 'POST':
        try:
            feature_order = ["MedInc", "HouseAge", "AveRooms", "AveBedrms",
                             "Population", "AveOccup", "Latitude", "Longitude"]
            values = []
            for feature in feature_order:
                # Convert form input to float
                values.append(float(request.form.get(feature)))
            features_df = pd.DataFrame([values], columns=feature_order)
            m = load_model()  # Lazy load the model
            prediction_log = m.predict(features_df)
            prediction = np.expm1(prediction_log[0])
            return render_template("predictui.html", prediction=prediction, form_data=request.form)
        except Exception as e:
            return render_template("predictui.html", error=str(e))
    else:
        return render_template("predictui.html")

# No __main__ block is needed; Gunicorn will import and run the app.
