from test import db
from flask_login import UserMixin
from flask_admin.contrib.sqla import ModelView
from flask_login import current_user
from flask import redirect, url_for
from werkzeug.security import generate_password_hash, check_password_hash

class Users(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True) # primary keys are required by SQLAlchemy
    username = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    admin = db.Column(db.Boolean, default=False)
    def is_admin(self):
        return admin

class Infected_france(UserMixin,db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date, unique=True)
    infected = db.Column(db.String(100))
    dead = db.Column(db.String(100))
    country_name = db.Column(db.String(255))

class MyModelView(ModelView):
    def is_accessible(self):
        return current_user.is_authenticated
    def inaccessible_callback(self, name, **kwargs):
        return redirect(url_for('auth.login'))
