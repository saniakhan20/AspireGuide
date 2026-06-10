from flask import Flask, request, jsonify
import joblib

app = Flask(__name__)

# Load the trained model
model = joblib.load("model.pkl")

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
    # Extract features from the input JSON
    features = [
        data['Openness'], data['Conscientiousness'], data['Extraversion'],
        data['Agreeableness'], data['Neuroticism'],
        data['Numerical'], data['Spatial'], data['Perceptual'],
        data['Abstract'], data['Verbal']
    ]
    # Make prediction
    prediction = model.predict([features])[0]
    return jsonify({'career': prediction})

if __name__ == "_main_":
    app.run(debug=True)
    
    