from flask import Flask, request, render_template, jsonify, send_file, send_from_directory
import io
from PIL import Image
from flask_cors import CORS
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from prophet import Prophet
import os

app = Flask(__name__)
CORS(app)
accuracy = 0.0

def forecast(file_name, p, f):
    global accuracy
    
    data = pd.read_csv(file_name)

    data['date'] = pd.to_datetime(data['date'])
    data = data.rename(columns={'date': 'ds', 'sales': 'y'})

    train_data = data[:-2]
    test_data = data[-2:]

    model = Prophet()
    model.fit(train_data)

    future = model.make_future_dataframe(periods=p, freq=f)
    forecast = model.predict(future)
   
    fig = model.plot(forecast, figsize=(9, 5))
    plt.xlabel('Time period')
    plt.ylabel('Sales')
    plt.savefig('plot.png')

    forecast.to_csv('forecast.csv', index=False)
    # Calculate accuracy
    y_true = test_data['y'].values
    y_pred = forecast['yhat'][-2:].values
    accuracy = 100 - np.mean(np.abs((y_true - y_pred) / y_true)) * 100
    print(accuracy)

@app.route('/', methods=['GET', 'POST'])
def hello_world():
    global accuracy 

    if request.method == 'POST':
        val1 = request.form['period']
        val2 = request.form['range']
        print(val1)
        print(val2)
        if val1 == "week":
            fre = "W"
        elif val1 == "month":
            fre = "M"
        elif val1 == "year":
            fre = "Y"
        elif val1 == "day":
            fre = "D"

        per = int(val2)

        file = request.files['file']
        file_name = file.filename
        file.save(file_name)
        file_size = len(file.read())
        file_stats = os.stat(file_name)

        forecast(file_name, per, fre)

        response_headers = {'Access-Control-Allow-Origin': '*'}
        response = {'message': 'Success', 'accuracy': accuracy * 100}
        return jsonify(response), 200, response_headers

    if request.method == 'GET':
        response = {'accuracy': accuracy * 100}
        return send_file('plot.png', mimetype='image/png'),response

@app.route('/accuracy', methods=['GET'])
def get_accuracy():
    global accuracy
    response = {'accuracy': accuracy}
    return jsonify(response)

if __name__ == '_main_':
    app.run(debug=True)


