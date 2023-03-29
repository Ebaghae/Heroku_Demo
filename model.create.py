#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import pickle
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split


# In[3]:


Coffee = pd.read_excel('C:/Users/14432/Downloads/Coffee_Cosumed.xlsx')


# In[4]:


Coffee.head()


# In[ ]:


#The data shows the seven days of the week and the cups of coffee drank on each day of the week along with the amount of cream and sugar used (teaspoons)


# In[5]:


#Linear Regression Model
X = Coffee[['Day_No.', 'Sugar_Cubes', 'Creamer_amount']]
y = Coffee['Coffee_drank']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=101)

lm = LinearRegression()
lm.fit(X_train,y_train)

pickle.dump(lm, open('model.pickle', 'wb'))



# In[6]:


from flask import Flask, jsonify, request



# In[8]:


#Create a flask app

app = Flask('Name')


# In[ ]:


@app.route('/', methods ['GET', 'POST'])
def home():
    if(request.method == 'GET'):
        data = "Hello"
        return jsonify({'data' : data})
    
    
@app.route('/predict/')
def coffee_consumed():
    model = pickle.load(open('model.pickle', 'rb'))
    Day_No. = request.args.get('Day_No.')
    Sugar_Cubes. = request.args.get('Sugar_Cubes')
    Creamer_amount = request.args.get('Creamer_amount')
    
    test_df = pd.Dataframe({'Day_No.':[Day_No.], 'Sugar_Cubes':[Sugar_Cubes], 'Creamer_Amount':[Creamer_amount]})
    coffee_cups = model.predict(test_df)
    return jsonify({'Coffee_drank':str(coffee_cups)})

app.run(debug-True)


