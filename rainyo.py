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
    try:
        x = json.loads(request.data)
        try:
            if x["raining"] == "true":
                return "It's raining, and I read the request."
            elif x["raining"] == "false":
                return "It's not raining, but I read the request."
            else:
                return "I don't know if it's raining, but I think I read the request."
        except Exception as e:
            return "Error: ", e
    except Exception as e:
        return "Error (early): ", e
                
                
#    if json.loads(request.data)["raining"] == "true":
#        r = requests.post("http://api.justyo.co/yoall/", data={'api_token': '3e795a3c-e627-1eef-41bb-cd7b0aee5f79'})
#        return "Yodeled.  Or at least you tried to."
#    else:
#        return "I'm not going to yo unless it's raining."


@app.route('/madison')
def visit_madison():
    return "Yo, want to know when it's raining in Madison?  Send a yo to MadisonRainYo."


if __name__ == "__main__":
    app.run()




