from flask import render_template, request, jsonify
from app import app, db
from app.models import Place

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', title='Home')

@app.route("/repair")
def repair():
    return render_template('repair.html', title='Repair')

@app.route('/add_place', methods=['POST'])
def add_place():
    data = request.get_json()
    place = Place(name=data['name'], latitude= data['latitude'], longitude= data['longitude'], picture= data['picture'], description= data['description'], tags= data['tags'])
    db.session.add(place)
    db.session.commit()
    return jsonify({'status': 'OK'})