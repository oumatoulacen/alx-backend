# Parametrize templates

Use the '_()' or 'gettext()' function to parametrize your templates. Use the message IDs home_title and home_header.

Create a babel.cfg file containing

[python: **.py]
[jinja2: **/templates/**.html]
extensions=jinja2.ext.autoescape,jinja2.ext.with_
Then initialize your translations with

$ pybabel extract -F babel.cfg -o messages.pot .
and your two dictionaries with

$ pybabel init -i messages.pot -d translations -l en
$ pybabel init -i messages.pot -d translations -l fr
Then edit files translations/[en|fr]/LC_MESSAGES/messages.po to provide the correct value for each message ID for each language. Use the following translations:

msgid	English	French
home_title	"Welcome to Holberton"	"Bienvenue chez Holberton"
home_header	"Hello world!"	"Bonjour monde!"
Then compile your dictionaries with

$ pybabel compile -d translations
Reload the home page of your app and make sure that the correct messages show up.