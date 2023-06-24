#!/usr/bin/python3
"""Script that starts flask web application"""
from flask import Flask
from markupsafe import escape
from flask import render_template

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def index():
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def c_is_awesome(text):
    new_text = text.replace('_', ' ')
    return f'C {escape(new_text)}'


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_page(text='is cool'):
    return f'Python {text.replace("_", " ")}'


@app.route('/number/<int:n>', strict_slashes=False)
def display_number(n):
    return f'{n} is a number'


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    return render_template('5-number.html', number=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def even_or_odd(n):
    if (n % 2 == 0):
        stat = 'even'
    else:
        stat = 'odd'
    return render_template('6-number_odd_or_even.html', num=n, stat=stat)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
