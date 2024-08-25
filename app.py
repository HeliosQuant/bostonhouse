import pickle
from flask import Flask, request, app, jsonify, url_for, render_template, redirect
import numpy as np
import pandas as pd

app = Flask(__name__)
with open("regression.pkl", "rb") as fileModel:
    model = pickle.load(fileModel)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/predict_api", methods=["POST"])
def predict_api():
    data = request.json['data']
    print(data)