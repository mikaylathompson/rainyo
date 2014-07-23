import os
import requests
import json
from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "Want to know when it's raining in Madison?  Send a yo to MADISONRAINYO"




@app.route('/madison')
def visit_madison():
    r = requests.post("http://api.justyo.co/yoall/", data={'api_token': '3e795a3c-e627-1eef-41bb-cd7b0aee5f79'})
    return "Yodeled.  Or at least you tried to."

@app.route('/madison', methods = ['POST'])
def rainyomadison():
    r = requests.post("http://api.justyo.co/yoall/", data={'api_token': '3e795a3c-e627-1eef-41bb-cd7b0aee5f79'})
    return "Yodeled.  Or at least you tried to."


if __name__ == "__main__":
    app.run()
