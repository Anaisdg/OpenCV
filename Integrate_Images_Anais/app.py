from flask import Flask, render_template, jsonify, redirect
from flask_pymongo import PyMongo
import Card_Predictor
import json

app = Flask(__name__)
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predictions')
def predictions():
    predictions = Card_Predictor.prediction_tuples()
  
    return jsonify(predictions)


if __name__ == "__main__":
    app.run(debug=True)
