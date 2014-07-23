import os
import requests
import json
from flask import Flask
from flask import request
from flask import render_template
import random

app = Flask(__name__)

@app.route('/')
def index():
    return visit_madison()

@app.route('/madison', methods = ['POST'])
def rainyomadison():
    x = json.loads(request.data)
    if x["raining"] == "true":
        r = requests.post("http://api.justyo.co/yoall/", data={'api_token': '3e795a3c-e627-1eef-41bb-cd7b0aee5f79'})
        return "Yodeled.  Or at least you tried to."
    elif x["raining"] == "false":
        return "It's not raining, so I'm not going to yo."
    else:
        return "Something's not right."
                
                

@app.route('/madison')
def visit_madison():
    imgs = ['hay_bales', 'dark_window', 'city_window']
    img = imgs[random.randint(0,2)] + "_sm.jpg"
    return render_template('madison.html', img = img)
    return "Yo, want to know when it's raining in Madison?  Send a yo to MadisonRainYo."


if __name__ == "__main__":
    app.run(debug=true)




