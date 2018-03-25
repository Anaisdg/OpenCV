from flask import *
import os
import pandas as pd
import json
from card_img_2 import rectify,preprocess,imgdiff,find_closest_card,getCards,get_training
from unpack import unpack
from werkzeug.utils import secure_filename
import sys

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
APP_ROOT = os.path.dirname(os.path.abspath(__file__))
UPLOAD_FOLDER = os.path.join(APP_ROOT, 'static/uploads')

ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])

app = Flask(__name__)


app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Debug
# print(app.config['UPLOAD_FOLDER'],file=sys.stderr)

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/', methods=['GET', 'POST'])
def upload_file():
   
    # Debug
    # print(request.method,file=sys.stderr)
    

    if request.method == 'POST':
        
        #Debug
        #print(request.files,file=sys.stderr)
        
        if request.files.get('file'):
        
            if 'file' not in request.files:
                flash('No file part')
                return redirect(request.url)
        file = request.files['file']
       
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):

            #debug
            # print(file.filename,file = sys.stderr)

            filename = secure_filename(file.filename)
            
            #Debug
            # print(filename,file=sys.stderr)

            #Debug
            #print((os.path.join(app.config['UPLOAD_FOLDER'], filename)),file=sys.stderr)
            
            file.save(os.path.join(UPLOAD_FOLDER, filename))
            return redirect(url_for('upload_file',
                                    filename=filename))
    return render_template("index.html")

@app.route("/fakedata")
def fakedata():
    data = unpack(test_list)
    return jsonify(data.to_dict(orient='records'))





if __name__ == '__main__':
    app.run(debug=True)
    