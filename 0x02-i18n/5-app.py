#!/usr/bin/env python3
'''' This is a simple web application that uses Flask to serve a web page.'''
import babel
from flask import Flask, g, render_template, request
from flask_cors import CORS
from flask_babel import Babel


app = Flask(__name__)


babel = Babel(app)
app.url_map.strict_slashes = False
CORS(app)


@babel.localeselector
def get_locale():
    ''' determines the best match supported language.'''
    lan = request.args.get('locale')
    if lan is not None and lan in app.config['LANGUAGES']:
        return lan
    return request.accept_languages.best_match(app.config['LANGUAGES'])


class Config:
    ''' This is the configuration for the app.'''
    DEBUG = False
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app.config.from_object(Config)


users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


def get_user(login_as: int):
    ''' returns a user dictionary or None if the ID cannot be found.'''
    if login_as in users:
        return users[login_as]
    return None


@app.before_request
def before_request():
    ''' This function sets the user if login_as is in the request.'''
    login_as = request.args.get('login_as')
    if login_as is not None:
        user = get_user(int(login_as))
        if user is not None:
            g.user = user
    else:
        g.user = None


@app.route('/')
def index():
    ''' This is the index page.'''
    return render_template('5-index.html', user=g.user)


if __name__ == '__main__':
    app.run(debug=True)
