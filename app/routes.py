from flask import render_template, request, redirect, url_for, flash
from app import app, db
from app.models import BikePart, Place, User
from app.forms import LoginForm, RegistrationForm
from flask_login import current_user, login_user, logout_user, login_required
import sqlalchemy as sa

# Home Page
@app.route('/')
@app.route('/index')
def index():
    parts = BikePart.query.all()
    return render_template('index.html', title="Home")

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

@app.route('/repair', methods=['GET', 'POST'])
def repair():
    # Get the category from the query parameters (default to 'Saddle' if not provided)
    category = request.args.get('category', 'Saddle')  # default to 'Saddle' category if no category is specified
    
    # Get the search term from the query parameters (if any)
    search_term = request.args.get('search', '')  # default to empty string if no search term is provided

    # Query for bike parts in the selected category and with the search term in the name or description
    if search_term:
        # Search for parts that match the search term in either the name or description
        parts = BikePart.query.filter(BikePart.category == category, 
                                      (BikePart.name.ilike(f'%{search_term}%') | 
                                       BikePart.description.ilike(f'%{search_term}%'))).all()
    else:
        # No search term, just get all parts in the category
        parts = BikePart.query.filter_by(category=category).all()
    
    # Render the template with the bike parts and the category
    return render_template('repair.html', parts=parts, category=category, search_term=search_term)


# Places Page
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