from flask import render_template, request, redirect, url_for
from app import app, db
from app.models import BikePart, Place

# Home Page
@app.route('/')
def index():
    return render_template('index.html', Title="Home")

# Parts Page
@app.route('/part/<int:part_id>')
def part_details(part_id):
    part = BikePart.query.get_or_404(part_id)
    return render_template('part_details.html', part=part)

@app.route('/add_part', methods=['GET', 'POST'])
def add_part():
    if request.method == 'POST':
        # Handle form submission and save the new part
        name = request.form['name']
        description = request.form['description']
        where_to_buy = request.form['where_to_buy']
        how_to_fix = request.form['how_to_fix']
        
        new_part = BikePart(name=name, description=description, where_to_buy=where_to_buy, how_to_fix=how_to_fix)
        db.session.add(new_part)
        db.session.commit()

        return redirect(url_for('repair'))  # Redirect to the repair page after adding a part

    return render_template('add_part.html')

@app.route("/repair")
def repair():
    parts = BikePart.query.all()
    print(parts)
    return render_template('repair.html', title='Repair', parts=parts)

# Places Page
@app.route('/add_place', methods=['POST'])
def add_place():
    data = request.get_json()
    place = Place(name=data['name'], latitude= data['latitude'], longitude= data['longitude'], picture= data['picture'], description= data['description'], tags= data['tags'])
    db.session.add(place)
    db.session.commit()
    return jsonify({'status': 'OK'})
