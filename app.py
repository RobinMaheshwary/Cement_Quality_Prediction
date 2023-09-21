from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
import pandas as pd
import joblib
import numpy as np

model = joblib.load('best_model.h5')

app = Flask(__name__)


@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        # Get input data from the HTML form
        input_data = {
            'Cement (component 1)(kg in a m^3 mixture)': float(request.form['cement']),
            'Blast Furnace Slag (component 2)(kg in a m^3 mixture)': float(request.form['blast_furnace_slag']),
            'Fly Ash (component 3)(kg in a m^3 mixture)': float(request.form['fly_ash']),
            'Water  (component 4)(kg in a m^3 mixture)': float(request.form['water']),
            'Superplasticizer (component 5)(kg in a m^3 mixture)': float(request.form['superplasticizer']),
            'Coarse Aggregate  (component 6)(kg in a m^3 mixture)': float(request.form['coarse_aggregate']),
            'Fine Aggregate (component 7)(kg in a m^3 mixture)': float(request.form['fine_aggregate']),
            'Age (day)': int(request.form['age'])
        }

        # Convert input data to a DataFrame
        input_df = pd.DataFrame([input_data])

        # Make a prediction using the loaded model
        prediction = model.predict(input_df)

        # Render the result page with the prediction
        return render_template('result.html', prediction=prediction[0])

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)