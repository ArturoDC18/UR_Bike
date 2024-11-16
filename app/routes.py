from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', title='Home')

@app.route("/repair")
def repair():
    return render_template('repair.html', title='Repair')