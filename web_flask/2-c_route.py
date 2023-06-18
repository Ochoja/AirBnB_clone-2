#!/usr/bin/python3
"""Using escape with flask"""
from markupsafe import escape
from flask import Flask


app = Flask(__name__)


@app.route("/c/<text>")
def c_text(text):
    return f"C {escape(text.replace('_', ' '))}"


@app.route("/")
def index():
    return "Hello HBNB!"


@app.route("/hbnb")
def hello():
    return "HBNB"
