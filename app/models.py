from app import db

# Bike Part Model
class BikePart(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    where_to_buy = db.Column(db.Text, nullable=False)
    how_to_fix = db.Column(db.Text, nullable=False)

# Initialize the database (Run this once to create the DB schema)
def init_db():
    db.create_all()
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
