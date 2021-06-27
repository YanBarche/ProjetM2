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

def get_infected_numbers():
    infected = db.session.execute("Select max(infected) as maximum, min(infected) as minimum from infected_france")
    for row in infected:
        avg = (int)((row[0]+row[1])/2)
        data ={ "maximum" : row[0], "minimum": row[1], "average":avg}
        return data

def get_dead_numbers():
    dead = db.session.execute("Select max(dead) as maximum, min(dead) as minimum from infected_france")
    for row in dead:
        avg = (int)((row[0]+row[1])/2)
        data ={ "maximum" : row[0], "minimum": row[1], "average":avg}
        return data