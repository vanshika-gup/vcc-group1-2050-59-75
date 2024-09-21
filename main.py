# app.py

from flask import Flask, request, jsonify, render_template
import pickle
import numpy as np

# Load the trained model
model_path = 'model.pkl'
with open(model_path, 'rb') as file:
    model = pickle.load(file)

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    # Extract data from form
    int_features = [int(x) for x in request.form.values()]
    final_features = [np.array(int_features)]
    
    # Make prediction
    prediction = model.predict(final_features)

    if prediction[0] == 0:
        output ="High income and low expenses, prospective customer for buisness growth"
    elif prediction[0] == 1:
        output ="Moderate income and moderate expenses, no special attention required"
    elif prediction[0] == 2:
        output ="High income and high expenses, no special attention required"
    elif prediction[0] == 3:
        output ="Low income and high expenses, risk to buisness"
    elif prediction[0] == 4:
        output ="Low income and low expenses, low chances of buisness"

    return render_template('index.html', prediction_text='Prediction: {}'.format(output))

if __name__ == "__main__":
    app.run(debug=True)
