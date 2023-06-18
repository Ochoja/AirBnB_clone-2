#!/usr/bin/python3
"""Flask Application"""
from flask import Flask


app = Flask(__name__)


@app.route("/", strict_slashes=False)
def index():
    """Print message when / is called"""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def home():
    """Print message when /hbnb is called"""
    return "HBNB"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
