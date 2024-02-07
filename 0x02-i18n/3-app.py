#!/usr/bin/env python3
'''' This is a simple web application that uses Flask to serve a web page.'''
import babel
from flask import Flask, render_template, request
from flask_cors import CORS
from flask_babel import Babel


app = Flask(__name__)
babel = Babel(app)
app.url_map.strict_slashes = False
CORS(app)


class Config:
    ''' This is the configuration for the app.'''
    DEBUG = False
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app.config.from_object(Config)


@babel.locale_selector
def get_locale():
    ''' determines the best match supported language.'''
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def index():
    ''' This is the index page.'''
    print('Hello World!')
    return render_template('1-index.html')


if __name__ == '__main__':
    app.run(debug=True)
