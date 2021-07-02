from flask import Blueprint, render_template,request
from flask_login import login_required, current_user
from utils import get_data_country, is_admin, get_infected_numbers,get_dead_numbers
import datetime
from models import Infected_france,Users
from test import db
main = Blueprint('main', __name__)
@main.route('/')
@main.route('/index')
def index():
    return render_template('index.html')

@main.route('/profile')
@login_required
def profile():
    return render_template('profile.html', name=current_user.username)

@main.route('/select')
@login_required
def select():
    return render_template('select.html')

@main.route('/select', methods=["POST"])
@login_required
def select_display():
    
    country = "France"
    if request.method == 'POST':
        country_name = request.form["country"]
   
    labels = [
    'JAN', 'FEB', 'MAR', 'APR',
    'MAY', 'JUN', 'JUL', 'AUG',
    'SEP', 'OCT', 'NOV', 'DEC'
    ]
   
    country = get_data_country(country_name)
    return render_template('line_test.html', country = country,labels=labels)

@main.route('/compare')
@login_required
def compare():
    return render_template('select_compare.html')

@main.route('/compare', methods=["POST"])
@login_required
def compare_display():
    country_name_first = request.form["country"]
    country_name_second = request.form["country2"]
    country = get_data_country(country_name_first)
    country2 = get_data_country(country_name_second)
    labels = [
    'JAN', 'FEB', 'MAR', 'APR',
    'MAY', 'JUN', 'JUL', 'AUG',
    'SEP', 'OCT', 'NOV', 'DEC'
    ]
    
    return render_template('compare.html', labels=labels,country=country, country2=country2)

@main.route('/filter')
@login_required
def filter():
    infected_numbers = get_infected_numbers()
    dead_numbers = get_dead_numbers()
    return render_template('filter.html',infected = infected_numbers, dead = dead_numbers)

@main.route('/filter', methods=["POST"])
@login_required
def filter_selected():
    infected = request.form["infected"]
    dead = request.form["dead"]
    date = request.form["date"]
    insertion = date.strftime("%m")
    month = (int)(insertion)
    countries = db.session.execute("Select country_name from infected_france")
    values=[]
    for country in countries:
        values.append(get_data_country(country[0]))
    print(values)
    return values[0]