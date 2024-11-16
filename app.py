from flask import Flask
from markupsafe import escape
app = Flask(__name__)

@app.route('/')
@app.route('/index/')
def main_view():
    return 'Hello, World!'

@app.route('/about')
def about_view():
    return 'This is an example of a different route.'

@app.route('/capitalize/<word>')
def capitalize_view(word):
    return '<h1>{}</h1>'.format(escape(word).capitalize())