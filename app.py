import os
import pickle
from flask import Flask, request, app, jsonify, url_for, render_template, redirect
import numpy as np
import pandas as pd

app = Flask(__name__)

with open("regression.pkl", "rb") as fileModel:
    regmodel = pickle.load(fileModel)

with open("scaling.pkl", "rb") as fileScalar:
    scalar = pickle.load(fileScalar)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/predict_api", methods=["POST"])
def predict_api():
    data = request.json['data']
    print(data)
    print(np.array(list(data.values())).reshape(1, -1))
    new_data = scalar.transform(np.array(list(data.values())).reshape(1, -1))
    output = regmodel.predict(new_data)
    print(output)
    return jsonify(output[0])
@app.route("/predict", methods=["POST"])
def predict():
    form_data = request.form
    data = [float(value) for ken,value in form_data.items()]
    print(data)
    final_input = scalar.transform(np.array(data).reshape(1, -1))
    print(final_input)
    output = regmodel.predict(final_input)[0]
    return render_template("home.html", prediction_text="The prediction is {}".format(output))

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000)) 
    app.run(debug=True, port=port)