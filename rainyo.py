import os
import requests
import json
from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "Want to know when it's raining in Madison?  Send a yo to MADISONRAINYO"



#@app.route('/madison', methods = ['POST'])
@app.route('/madison')
def rainyomadison():
    
    r = requests.post("http://api.justyo.co/yoall/", data={'api_token': '3e795a3c-e627-1eef-41bb-cd7b0aee5f79'})
    
    if 'result' in r.json() and r.json()['result'] == 'OK':
        return json.dumps({'text': 'Notified Madisonians of rain'})
    else:
        return json.dumps({'text': 'Error sending Yo.  Everyone\'s going to get wet now...'})
    


if __name__ == "__main__":
    app.run()