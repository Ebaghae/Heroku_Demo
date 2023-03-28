#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle


# In[4]:


app = Flask('Name')
model = pickle.load(open('model.pickle', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict/', methods = ['POST'])
def predict():
    
    int_features = [eval(x) for x in request.form.values()]
    final_features = [np.array(int_features)]
    prediction = model.predict(final_features)
    
    output = np.round(prediction[0], 2)
    
    return render_template('index.html', prediction_text = "Coffee Consumed: {} Cups".format(output[0]))

if Flask('Name') == "Main":
    app.run(debug=True)


# In[ ]:





# In[ ]:




