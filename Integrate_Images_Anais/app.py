from flask import Flask, render_template, jsonify, redirect
from flask_pymongo import PyMongo
import Card_Predictor
import json
import pandas as pd

app = Flask(__name__)
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predictions')
def prediction():
    card_predictions = Card_Predictor.prediction_tuples()
    folderpath = 'static/images/cropped'
    images = Card_Predictor.find_cropped_images(folderpath)
    dictionary = {'card_predictions':card_predictions, 'images':images}
    print(card_predictions)
    print(images)
    return render_template('predictions.html', card_predictions = card_predictions, images= images)


if __name__ == "__main__":
    app.run(debug=True)
