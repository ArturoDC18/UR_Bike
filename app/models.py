from app import db, login
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from sqlalchemy.sql import func

# Bike Part Model
class BikePart(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    where_to_buy = db.Column(db.Text, nullable=False)
    how_to_fix = db.Column(db.Text, nullable=False)

class Place(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), index=True)
    latitude = db.Column(db.Float)
    longitude = db.Column(db.Float)
    picture = db.Column(db.String(128))
    description = db.Column(db.String(128))
    tags = db.Column(db.String(128))

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
    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    @login.user_loader
    def load_user(id):
        return db.session.get(User, int(id))