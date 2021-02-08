from flask import Blueprint, render_template,request
from flask_login import login_required, current_user
from utils import get_data_country, is_admin
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
def select():
    return render_template('select.html')

@main.route('/select', methods=["POST"])
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
def compare():
    return render_template('select_compare.html')

@main.route('/compare', methods=["POST"])
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
