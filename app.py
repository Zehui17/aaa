#!/usr/bin/env python
# coding: utf-8

# In[ ]:





# In[1]:


from flask import Flask, render_template, request
app = Flask(__name__)


# In[2]:


import  joblib


@app.route("/", methods = ["GET", "POST"])
def index():
    if request.method == 'POST':
        rates = float(request.form.get('rates'))
        print(rates)
        model1 = joblib.load('regression_DBS')
        r1 = model1.predict([[rates]])
        model2 = joblib.load("tree_DBS")
        r2 = model2.predict([[rates]])
        return (render_template('index.html', result1 = r1, result2 = r2))
    else:
        return (render_template('index.html', result1 = 'waiting', result2 = 'waiting'))


# In[ ]:


if __name__ == "__main__":
    app.run()


# In[ ]:


#app.run(host = '127.0.0.1', port = int("80"))


# In[ ]:




