from currency_formater import *
from flask import Flask

app = Flask(__name__)


@app.route("/format/<number>")
def hello_world(number):
    return { "formated": currency_format(number)}

