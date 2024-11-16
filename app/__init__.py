from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://admin:rbUWeKiW44O4o1egPHwd@recs-db.cn62c4wqs8na.us-east-2.rds.amazonaws.com:3306/recs-db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

from app import routes