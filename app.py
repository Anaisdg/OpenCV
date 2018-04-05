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
import Gamelogic


ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'static/images/Original'

result = []
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
            print(cards, )
            board = unpack.unpack_result(cards)
            foundSet = Gamelogic.findSet(board)
            result.append(foundSet)
        return redirect('results')
    return render_template("index.html")

@app.route('/results')
def ending():
    return render_template('results.html')

@app.route("/fakedata")
def fakedata():
  
    return jsonify(result)





if __name__ == '__main__':
    app.run(debug=True)
    