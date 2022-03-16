from flask import Flask
from flask import Response
from flask import request
import joblib
import pandas as pd
import json
import numpy as np

# model = None
app = Flask(__name__)

@app.route('/')
def home_endpoint():
    return 'Welcome to CodeClan'

@app.route('/predict', methods=['POST'])
def predict_endpoint():
    data = request.json
    features = np.array(json.loads(data['features']))
    preds = (
        model
        .predict(features)
        .tolist()
    )
    response = json.dumps(preds)
    return Response(response, status=200, mimetype="application/json")

if __name__ == '__main__':
    model = joblib.load('log_model.joblib')
    app.run(host='0.0.0.0', port=80)
