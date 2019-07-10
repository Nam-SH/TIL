from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello world!"

@app.route("/ssafy")
def ssafy():
    return "This is ssafy, 1+1=?"