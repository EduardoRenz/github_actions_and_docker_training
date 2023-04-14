from currency_formater import *
from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return { "message": "This is root"}

@app.route("/format/<number>")
def format(number):
    return { "formated": currency_format(number)}

