import keras
from keras.preprocessing import image
from keras.applications.xception import (Xception, preprocess_input, decode_predictions)
from keras import models
from keras.models import load_model
from keras.models import Sequential
from keras.layers import Conv2D, MaxPooling2D
from keras.layers import Activation, Dropout, Flatten, Dense

import numpy as np
import pandas as pd
import os

class_list = ['1DGE',
 '1DGF',
 '1DGS',
 '1DPE',
 '1DPF',
 '1DPS',
 '1DRE',
 '1DRF',
 '1DRS',
 '1OGE',
 '1OGF',
 '1OGS',
 '1OPE',
 '1OPF',
 '1OPS',
 '1ORE',
 '1ORF',
 '1ORS',
 '1SGE',
 '1SGF',
 '1SGS',
 '1SPE',
 '1SPF',
 '1SPS',
 '1SRE',
 '1SRF',
 '1SRS',
 '2DGE',
 '2DGF',
 '2DGS',
 '2DPE',
 '2DPF',
 '2DPS',
 '2DRE',
 '2DRF',
 '2DRS',
 '2OGE',
 '2OGF',
 '2OGS',
 '2OPE',
 '2OPF',
 '2OPS',
 '2ORE',
 '2ORF',
 '2ORS',
 '2SGE',
 '2SGF',
 '2SGS',
 '2SPE',
 '2SPF',
 '2SPS',
 '2SRE',
 '2SRF',
 '2SRS',
 '3DGE',
 '3DGF',
 '3DGS',
 '3DPE',
 '3DPF',
 '3DPS',
 '3DRE',
 '3DRF',
 '3DRS',
 '3OGE',
 '3OGF',
 '3OGS',
 '3OPE',
 '3OPF',
 '3OPS',
 '3ORE',
 '3ORF',
 '3ORS',
 '3SGE',
 '3SGF',
 '3SGS',
 '3SPE',
 '3SPF',
 '3SPS',
 '3SRE',
 '3SRF',
 '3SRS']

model_path = 'static/model/first_try.h5'
image_size = (150, 150)
folderpath = 'static/images/cropped'

#Create Model and Load Weights

model = Sequential()
model.add(Conv2D(32, (3, 3), input_shape=(150, 150, 3)))
model.add(Activation('relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))

model.add(Conv2D(32, (3, 3)))
model.add(Activation('relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))

model.add(Conv2D(64, (3, 3)))
model.add(Activation('relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))

model.add(Flatten())
model.add(Dense(64))
model.add(Activation('relu'))
model.add(Dropout(0.5))
model.add(Dense(81))
model.add(Activation('softmax'))

model.compile(loss='categorical_crossentropy',
              optimizer='adam',
              metrics=['accuracy'])

model.load_weights(model_path)

# Predict the image

def predictor(image_path):
    img = image.load_img(image_path, target_size=image_size)
    x = image.img_to_array(img)
    # print(x.shape)
    x = np.expand_dims(x, axis=0)
    x = preprocess_input(x)
    predictions = model.predict(x)
    # print(max(predictions[0]))
    list_a = predictions[0]
    list_b = class_list
    zip_test = list(zip(list_a, list_b))
    return max(zip_test)

def find_cropped_images(folderpath):
    return [folderpath + '/' + v for v in os.listdir(folderpath) if v != '.DS_Store']

def prediction_tuples():
     predictions = [predictor(png) for png in find_cropped_images(folderpath)]
     predictions = pd.Series(predictions).to_json(orient='values')
     return predictions

print(prediction_tuples())
