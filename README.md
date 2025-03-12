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


   # California Housing Price Prediction API

## Project Overview
This project provides an API for predicting house prices in California based on various features such as median income, house age, and geographic location. The model used is a fine-tuned **RandomForestRegressor**, optimized for performance and accuracy. The API is deployed using Flask, Docker, and Render.

## Developer Information
- **Author:** Rehan Khan
- **Email:** [rehankhanpro78@gmail.com](mailto:rehankhanpro78@gmail.com)
- **GitHub Repository:** [Rehan Khan SoulAI](https://github.com/rehanpro78/rehan_khan_soulai)

## Model Details
- **Algorithm:** RandomForestRegressor
- **Hyperparameter Tuning:** GridSearchCV
- **Evaluation Metrics:** Mean Absolute Error (MAE), Mean Squared Error (MSE), R-squared (R²)
- **Performance:**
  - **MAE:** 0.48
  - **MSE:** 0.36
  - **R² Score:** 0.89

## API Endpoints
### 1. **Home Page** (`GET /`)
Displays project details, API usage instructions, and a link to the interactive UI.

### 2. **Prediction API** (`POST /predict`)
Accepts JSON input and returns the predicted house price.

#### Example Request:
```json
{
  "MedInc": 8.0,
  "HouseAge": 30,
  "AveRooms": 5.0,
  "AveBedrms": 1.0,
  "Population": 1000,
  "AveOccup": 3.0,
  "Latitude": 37.0,
  "Longitude": -120.0
}
```

#### Example Response:
```json
{
  "prediction": 250000.00
}
```

### 3. **Interactive UI** (`GET/POST /predictui`)
A web-based interface for entering feature values and receiving predictions interactively.

## How to Test the API
### Using cURL
```sh
curl -X POST "https://rehan-khan-soulai.onrender.com/predict" \
-H "Content-Type: application/json" \
-d '{"MedInc": 8.0, "HouseAge": 30, "AveRooms": 5.0, "AveBedrms": 1.0, "Population": 1000, "AveOccup": 3.0, "Latitude": 37.0, "Longitude": -120.0}'
```

### Using Python (requests library)
```python
import requests
import json

url = "https://rehan-khan-soulai.onrender.com/predict"
data = {
    "MedInc": 8.0,
    "HouseAge": 30,
    "AveRooms": 5.0,
    "AveBedrms": 1.0,
    "Population": 1000,
    "AveOccup": 3.0,
    "Latitude": 37.0,
    "Longitude": -120.0
}
response = requests.post(url, json=data)
print(response.json())
```

### Using PowerShell
```powershell
Invoke-RestMethod -Method Post `
    -Uri "https://rehan-khan-soulai.onrender.com/predict" `
    -ContentType "application/json" `
    -Body '{"MedInc": 8.0, "HouseAge": 30, "AveRooms": 5.0, "AveBedrms": 1.0, "Population": 1000, "AveOccup": 3.0, "Latitude": 37.0, "Longitude": -120.0}'
```

## Deployment
- **Platform:** Render
- **Containerization:** Docker
- **Model Storage:** joblib file (`tuned_rf_model.joblib`)
- **Port Binding:** `10000`

## Future Improvements
- Implement authentication for API access.
- Enhance model accuracy with additional feature engineering.
- Deploy a React-based UI for better user interaction.

For more details, refer to the [GitHub Repository](https://github.com/rehanpro78/rehan_khan_soulai).
