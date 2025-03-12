from flask import Flask, request, jsonify, render_template
import joblib
import numpy as np

app = Flask(__name__)

# Global variable for lazy model loading
model = None

def load_model():
    global model
    if model is None:
        # Load the model with memory mapping to reduce peak memory usage
        model = joblib.load("tuned_rf_model.joblib", mmap_mode='r')
    return model

# Index route to serve the landing page (templates/index.html)
@app.route('/')
def index():
    return render_template("index.html")

# Prediction endpoint that expects JSON input and returns a predicted price
@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.get_json()
        feature_order = [
            "MedInc", "HouseAge", "AveRooms", "AveBedrms",
            "Population", "AveOccup", "Latitude", "Longitude"
        ]
        features = [data.get(feature) for feature in feature_order]
        features_array = np.array(features).reshape(1, -1)
        m = load_model()  # Lazy load the model on first request
        prediction_log = m.predict(features_array)
        # Convert the prediction from log-scale back to the original scale
        prediction = np.expm1(prediction_log[0])
        return jsonify({'predicted_price': prediction})
    except Exception as e:
        return jsonify({'error': str(e)})
