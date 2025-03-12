from flask import Flask, request, jsonify
import joblib
import numpy as np

app = Flask(__name__)
model = None

def load_model():
    global model
    if model is None:
        model = joblib.load("tuned_rf_model.joblib")
    return model

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.get_json()
        feature_order = ["MedInc", "HouseAge", "AveRooms", "AveBedrms", "Population", "AveOccup", "Latitude", "Longitude"]
        features = [data.get(feature) for feature in feature_order]
        features_array = np.array(features).reshape(1, -1)
        m = load_model()  # load the model on the first request
        prediction_log = m.predict(features_array)
        prediction = np.expm1(prediction_log[0])
        return jsonify({'predicted_price': prediction})
    except Exception as e:
        return jsonify({'error': str(e)})








"""from flask import Flask, request, jsonify
import joblib
import numpy as np

# Load the saved tuned Random Forest model
model = joblib.load("tuned_rf_model.joblib")

app = Flask(__name__)

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.get_json()
        feature_order = ["MedInc", "HouseAge", "AveRooms", "AveBedrms", "Population", "AveOccup", "Latitude", "Longitude"]
        features = [data.get(feature) for feature in feature_order]
        features_array = np.array(features).reshape(1, -1)
        
        # Predict (model output is log-transformed; convert it back)
        prediction_log = model.predict(features_array)
        prediction = np.expm1(prediction_log[0])
        return jsonify({'predicted_price': prediction})
    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
"""
