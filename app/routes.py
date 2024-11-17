from flask import render_template, request, redirect, url_for, flash
from app import app, db
from app.models import BikePart, Place, User
from app.forms import LoginForm, RegistrationForm
from flask_login import current_user, login_user, logout_user, login_required
import sqlalchemy as sa

@app.route('/')
@app.route('/index')
def index():
    parts = BikePart.query.all()
    return render_template('index.html', title="Home")

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

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = db.session.scalar(
            sa.select(User).where(User.username == form.username.data))
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        login_user(user)
        return redirect(url_for('index'))
    return render_template('login.html', title='Sign In', form=form)
@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Congratulations, you are now a registered user!')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)
@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))