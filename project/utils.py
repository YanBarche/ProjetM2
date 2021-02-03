import datetime
from models import Infected_france
from test import db

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