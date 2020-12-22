from flask import Blueprint, render_template
from flask_login import login_required, current_user
from db_loging import Connection_Database,get_data
import datetime
main = Blueprint('main', __name__)
@main.route('/index')
def index():
    return render_template('index.html')

@main.route('/profile')
@login_required
def profile():
    return render_template('profile.html', name=current_user.username)

@main.route('/line')
def line():
    result = get_data("Infected_france")
    labels = [
    'JAN', 'FEB', 'MAR', 'APR',
    'MAY', 'JUN', 'JUL', 'AUG',
    'SEP', 'OCT', 'NOV', 'DEC'
    ]
    values_infected = [0,0,0,0,0,0,0,0,0,0,0,0]
    values_dead = [0,0,0,0,0,0,0,0,0,0,0,0]
    for row in result:
        insertion = row[1].strftime("%m")
        #datee = datetime.datetime.strptime(insertion, "%Y-%m-%d")
        month = (int)(insertion)
        infected = row[2]
        dead = row[3]
        values_infected[month-1] += infected
        values_dead[month-1] += dead
    print(values_infected)
    return render_template('line_test.html', title='', max=50000, labels=labels, values=values_infected)

@main.route('/compare')
def compare():
    result = get_data("Infected_france")
    labels = [
    'JAN', 'FEB', 'MAR', 'APR',
    'MAY', 'JUN', 'JUL', 'AUG',
    'SEP', 'OCT', 'NOV', 'DEC'
    ]
    values_infected = [0,0,0,0,0,0,0,0,0,0,0,0]
    values_dead = [0,0,0,0,0,0,0,0,0,0,0,0]
    for row in result:
        insertion = row[1].strftime("%m")
        #datee = datetime.datetime.strptime(insertion, "%Y-%m-%d")
        month = (int)(insertion)
        infected = row[2]
        dead = row[3]
        values_infected[month-1] += infected
        values_dead[month-1] += dead
    print(values_infected)
    return render_template('compare.html', title='', max=50000, labels=labels, values=values_infected,dead=values_dead)

