import numpy as np
import pandas as pd
from flask import Flask, request, jsonify, render_template, Flask
from flask_restful import Resource, Api, reqparse
import pickle

import sys
sys.path.insert(0, '/home/henri/Documents/Lighthouse-lab/lighthouse-data-notes')
import ccf_module as ccf

app = Flask(__name__)
model = pickle.load(open('pickledRandCVModel.sav', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
    # so html forms only return strings
    #numpy, unlike list only store one data type (nums or str or num and char)
    features = [x for x in request.form.values()]
    num_features = list()
    for i in range(len(features)):
        if 5 <= i <= 9:
            num_features.append(int(features[i]))
        else:
            num_features.append(features[i])
    print(num_features)

    ds = pd.Series(num_features,index=['Gender','Married','Dependents','Education','Self_Employed','ApplicantIncome','CoapplicantIncome','LoanAmount','Loan_Amount_Term','Credit_History','Property_Area',])
    #All the bloody stack overflow are asking you to change your mixed data to an np array but numpy does not handle multiple dtypes like list or pd.df.
    #if you change your single observation into a dataframe using df.to_frame() then transposing it so that it matches
    
    prediction = model.predict(ds.to_frame().T)
    output = prediction[0]

    return render_template('index.html', prediction_text=f'For the values: {num_features}, the answer: {output}')

@app.route('/predict_api',methods=['POST'])
def predict_api():
    json_data = request.get_json()
    df = pd.DataFrame(json_data.values(), index=json_data.keys()).transpose()
    # getting predictions from our model.
    # it is much simpler because we used pipelines during development
    res = model.predict_proba(df)
    # we cannot send numpt array as a result
    return res.tolist() 


if __name__ == '__main__':
    app.run(host="0.0.0.0",port=5004,debug=True)
#http://0.0.0.0:5001/calculator?operation=add&num=69&num2=420\