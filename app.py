print("Starting Flask app...")

from flask import Flask, render_template, request
import numpy as np
import joblib
import os

# Initialize the Flask app
app = Flask(__name__)

# Load the trained model
model = joblib.load(os.path.join('model', 'model.pkl'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get values from the form
        spx = float(request.form['spx'])
        uso = float(request.form['uso'])
        slv = float(request.form['slv'])
        euro_usd = float(request.form['eurousd'])

        # Create a feature array in the right order
        features = np.array([[spx, uso, slv, euro_usd]])

        # Predict using the model
        prediction = model.predict(features)[0]
        prediction = round(prediction, 2)

        return render_template('index.html', prediction_text=f"Predicted Gold Price: ${prediction}")

    except Exception as e:
        return render_template('index.html', prediction_text=f"Error: {str(e)}")

if __name__ == '__main__':
    app.run(debug=True)
