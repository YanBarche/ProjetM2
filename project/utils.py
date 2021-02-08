import datetime
from models import Infected_france,Users
from test import db
from flask_login import current_user
from functools import wraps
def get_data_country(Name):
    result = db.session.query(Infected_france).filter_by(country_name = Name).all()
    values_infected = [0,0,0,0,0,0,0,0,0,0,0,0]
    values_dead = [0,0,0,0,0,0,0,0,0,0,0,0]
    for row in result:
        insertion = row.date.strftime("%m")
        month = (int)(insertion)
        infected = row.infected
        dead = row.dead
        values_infected[month-1] += infected
        values_dead[month-1] += dead
       
    country={'name':Name,'values_infected':values_infected,'values_dead':values_dead}
    return country
def is_admin():
    user = Users.query.filter_by(id = current_user.get_id()).first()
    if user is None:
        return False
    return user.admin
