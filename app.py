# -*- coding: utf-8 -*-
"""
Created on Thu Jul 16 20:32:38 2020

@author: Raj
"""
import numpy as np
from flask import Flask, request, jsonify, render_template


app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
    '''
    For rendering results on HTML GUI
    '''
    #int_features = [x for x in request.form.values()]
    input=request.form.values()[1]
    
    return render_template('index.html', prediction_text=input)


if __name__ == "__main__":
    app.run(debug=True)