from flask import *
import os
import pandas as pd
import json
from werkzeug.utils import secure_filename
import sys
from gamelogic import *
from unpack import *

test_list = [['1','D','R','S'],
             ['2','D','P','E'],
             ['3','D','P','E'],
             ['1','D','P','E'],
            ['2','S','G','S'],
            ['2','O','G','E'],
            ['2','D','P','E'],
            ['3','D','R','F'],
            ['1','O','R','F'],
            ['2','O','R','F'],
            ['3','O','R','F'],
            ['1','D','R','F'],
            ['2','D','R','F'],
            ['3','D','R','F'],
            ['1','S','G','F'],
            ['2','S','G','F']]


ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])

app = Flask(__name__)

result = []
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/', methods=['GET', 'POST'])
def upload_file():

    if request.method == 'POST':
        if request.files.get('file'):
            cards = test_list
            board = unpack_dict(cards)
            foundSet = findSet(board)
            # file = request.files['file']
            # image = file.read()
            
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
    