#!/usr/bin/python3
"""Flask Application"""
from flask import Flask
from markupsafe import escape


app = Flask(__name__)


@app.route("/c/<text>", strict_slashes=False)
def c_text(text):
    return f"C {escape(text.replace('_', ' '))}"


@app.route("/", strict_slashes=False)
def index():
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hello():
    return "HBNB"


@app.route('/python', strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def python(text='is cool'):
    return f"Python {escape(text.replace('_', ' '))}"


@app.route("/number/<int:n>", strict_slashes=False)
def number(n):
    return f"escape({n}) is a number"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
