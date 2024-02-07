#!/usr/bin/env python3
'''' This is a simple web application that uses Flask to serve a web page.'''
import babel
from flask import Flask, render_template
from flask_cors import CORS
from flask_babel import Babel  # type: ignore

app = Flask(__name__)
babel = Babel(app)
app.url_map.strict_slashes = False

@app.route('/')
def index():
    ''' This is the index page.'''
    print('Hello World!')
    return render_template('0-index.html')

if __name__ == '__main__':
    app.run(debug=True)