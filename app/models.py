from app import db

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
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    admin = db.Column(db.Boolean, default=False)
    password_hash = db.Column(db.String(128))

    def __repr__(self):
        return '<User {}>'.format(self.username)