import os
import requests
import json
from flask import Flask
from flask import request

app = Flask(__name__)

@app.route('/')
def index():
    return "Want to know when it's raining in Madison?  Send a yo to MadisonRainYo"

@app.route('/madison', methods = ['POST'])
def rainyomadison():
    if request.get_json(force=True)["raining"] == "true":
        r = requests.post("http://api.justyo.co/yoall/", data={'api_token': '3e795a3c-e627-1eef-41bb-cd7b0aee5f79'})
        return "Yodeled.  Or at least you tried to."
    else:
        return "I'm not going to yo unless it's raining."


@app.route('/madison')
def visit_madison():
    return "Yo, want to know when it's raining in Madison?  Send a yo to MadisonRainYo."


if __name__ == "__main__":
    app.run()




