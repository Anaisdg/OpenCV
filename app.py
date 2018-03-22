from flask import Flask, jsonify, render_template
import pandas as pd
import json
from card_img_2 import rectify,preprocess,imgdiff,find_closest_card,getCards,get_training
from unpack import unpack

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

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("**")

@app.route("/fakedata")
def fakedata():
    data = unpack(test_list)
    return jsonify(data.to_dict(orient='records'))


if __name__ == '__main__':
    app.run(debug=True)
    