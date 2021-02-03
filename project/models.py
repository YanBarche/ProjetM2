from test import db
from flask_login import UserMixin

class Users(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True) # primary keys are required by SQLAlchemy
    username = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))

class Infected_france(UserMixin,db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date, unique=True)
    infected = db.Column(db.String(100))
    dead = db.Column(db.String(100))
    country_name = db.Column(db.String(255))

