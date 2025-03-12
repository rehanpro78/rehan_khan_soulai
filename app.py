from flask import Flask, request, jsonify, Blueprint, render_template
import joblib
import numpy as np

app = Flask(__name__)
model = None  # Global variable for lazy loading

def load_model():
    global model
    if model is None:
        # Load the model with memory mapping to reduce peak memory usage
        model = joblib.load("tuned_rf_model.joblib", mmap_mode='r')
    return model

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Expected JSON: 
        # {"MedInc": 8.0, "HouseAge": 30, "AveRooms": 5.0, "AveBedrms": 1.0, 
        #  "Population": 1000, "AveOccup": 3.0, "Latitude": 37.0, "Longitude": -120.0}
        data = request.get_json()
        feature_order = ["MedInc", "HouseAge", "AveRooms", "AveBedrms", "Population", "AveOccup", "Latitude", "Longitude"]
        features = [data.get(feature) for feature in feature_order]
        features_array = np.array(features).reshape(1, -1)
        
        # Lazy load the model using memory mapping
        m = load_model()
        prediction_log = m.predict(features_array)
        # Inverse the log1p transformation
        prediction = np.expm1(prediction_log[0])
        
        return jsonify({'predicted_price': prediction})
    except Exception as e:
        return jsonify({'error': str(e)})


# Create a Blueprint for the index page
index_bp = Blueprint('index', __name__, template_folder='templates')

@index_bp.route('/')
def index():
    return render_template('index.html')
