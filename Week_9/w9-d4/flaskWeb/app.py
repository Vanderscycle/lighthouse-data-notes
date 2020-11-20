import numpy as np
import pandas as pd

import pickle
import jieba

from flask import Flask, request, jsonify, render_template, Flask
from flask_restful import Resource, Api, reqparse

import sys
sys.path.insert(0, '/home/henri/Documents/Lighthouse-lab/lighthouse-data-notes')
import ccf_module as ccf

from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.sequence import pad_sequences

chineseEncoder = pickle.load(open('/home/henri/Documents/Lighthouse-lab/lighthouse-data-notes/Week_9/w9-d4/zhongTokenizer.sav', 'rb'))
engEncoder = pickle.load(open('/home/henri/Documents/Lighthouse-lab/lighthouse-data-notes/Week_9/w9-d4/engTokenizer.sav', 'rb'))
model = load_model('/home/henri/Documents/Lighthouse-lab/Databases/w9-d4-db/cnn-eng')

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():

    features = request.form.values() #there's liek only one value
    encodedFeatures = ccf.encode_sequences(chineseEncoder, 12, features).T
    predTestSentence = model.predict_classes(encodedFeatures)
    output = ccf.decoder(predTestSentence,engEncoder)
    
    return render_template('index.html', prediction_text=f'For the values: {features}, the answer: {output}')

if __name__ == '__main__':
    app.run(host="0.0.0.0")#,port=5099,debug=True)
#http://0.0.0.0:5001/calculator?operation=add&num=69&num2=420\