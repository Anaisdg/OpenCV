from flask import *
import os
import pandas as pd
import json
from werkzeug.utils import secure_filename
import sys
import unpack
import card_detection 
import cv2 as cv
import Card_Predictor 
import gamelogic


ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])

folderpath = 'static/images/cropped'

result = []

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'static/images/Original'



def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/', methods=['GET', 'POST'])
def upload_file():

    if request.method == 'POST':
        if request.files.get('file'):
            file= request.files['file']
            
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], "original.jpg"))
            
            numcards = 12
            card_detection.Imagedetection("static/images/Original/original.jpg",numcards)
            cards= Card_Predictor.prediction_tuples()
            
            board = unpack.unpack_result(cards)
            foundSet = gamelogic.findSet(board)
            result.append(foundSet)
        return redirect('results')
    return render_template("index.html")

@app.route('/results')
def ending():
    card_predictions = Card_Predictor.prediction_tuples()
    folderpath = 'static/images/cropped'
    images = Card_Predictor.find_cropped_images(folderpath)
    dictionary = {'card_predictions':card_predictions, 'images':images}
    return render_template('results.html', card_predictions = card_predictions, images= images)
    

@app.route("/fakedata")
def fakedata():
  
    return jsonify(result)





if __name__ == '__main__':
    app.run(debug=True)
    