import os
import requests
import json
from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "Want to know when it's raining in Madison?  Send a yo to MADISONRAINYO"

@app.route('/madison', methods = ['POST'])
def rainyomadison():
    r = requests.post("http://api.justyo.co/yoall/", data={'api_token': '3e795a3c-e627-1eef-41bb-cd7b0aee5f79'})
    return "Yodeled.  Or at least you tried to."

yo_button = """<head><title>Madison RainYo</title></head>
    <body>
    <script type="text/javascript">
    	var _yoData = {
	    	"username": "MADISONRAINYO",
	    	"trigger": "it's raining in Madison"
	    };
	    var s = document.createElement("script");
	    s.type = "text/javascript";
    	s.src = "//yoapp.s3.amazonaws.com/js/yo-button.js";
	    (document.head || document.getElementsByTagName("head")[0]).appendChild(s);
    </script>
    <div id="yo-button"></div>
    </body>"""


@app.route('/madison')
def visit_madison():
    return yo_button


if __name__ == "__main__":
    app.run()




