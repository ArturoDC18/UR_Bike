from flask import render_template, request, redirect, url_for
from app import app, db
from app.models import BikePart, Place

@app.route('/')
def index():
    parts = BikePart.query.all()
    return render_template('index.html', parts=parts)

@app.route('/part/<int:part_id>')
def part_details(part_id):
    part = BikePart.query.get_or_404(part_id)
    return render_template('part_details.html', part=part)

@app.route('/add', methods=['GET', 'POST'])
def add_part():
    if request.method == 'POST':
        new_part = BikePart(
            name=request.form['name'],
            description=request.form['description'],
            where_to_buy=request.form['where_to_buy'],
            how_to_fix=request.form['how_to_fix']
        )
        db.session.add(new_part)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('add_part.html')
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
