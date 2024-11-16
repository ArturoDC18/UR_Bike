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
