from app import db

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