import os
import requests
import json
import random
from flask import Flask, request, render_template

app = Flask(__name__)
if __name__ == "__main__":
    app.run()

@app.route('/')
def index():                # index redirects to madison page
    return visit_madison()

@app.route('/madison')
def visit_madison():
    #pick a random image for the background
    imgs = ['hay_bales', 'dark_window', 'city_window']
    img = imgs[random.randint(0,2)] + "_sm.jpg"
    #render the page
    return render_template('madison.html', img = img)


@app.route('/madison', methods = ['POST'])
def rainyomadison():
    x = json.loads(request.data)
    with open('yo_api.json', 'r') as f:
        data = json.load(f)
    if x["raining"] == "true":
        r = requests.post("http://api.justyo.co/yoall/", data=data)
        return "Yodeled.  Or at least tried to."
    elif x["raining"] == "false":
        return "It's not raining, so no yo."
    else:
        return "Something's went wrong."
                