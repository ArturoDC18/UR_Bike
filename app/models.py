from app import db, login
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from sqlalchemy.sql import func

# Bike Part Model
class BikePart(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(200))
    price = db.Column(db.Float)
    buy_link = db.Column(db.String(200))  # New field for Where to Buy link
    category = db.Column(db.String(100))
    
    def __repr__(self):
        return f'<BikePart {self.name}>'

class Place(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), index=True)
    latitude = db.Column(db.Float)
    longitude = db.Column(db.Float)
    picture = db.Column(db.String(128), nullable = True)
    description = db.Column(db.String(128))
    parking = db.Column(db.Boolean, default=False)
    repair = db.Column(db.Boolean, default=False)
    recommendation = db.Column(db.Boolean, default=False)

    def __repr__(self):
        return '<Place {}>'.format(self.name)
        
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    admin=db.Column(db.Boolean, default=False)

    def __repr__(self):
        return '<User {}>'.format(self.username)
    def set_password(self, password):
        self.password_hash = generate_password_hash(password)
    def set_admin(self):
        self.admin=True
    def is_admin(self):
        return self.admin
    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    @login.user_loader
    def load_user(id):
        return db.session.get(User, int(id))