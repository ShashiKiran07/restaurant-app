from application.models import Dish
from flask import Blueprint, render_template, redirect, flash, request
from application.models import Dish

main = Blueprint('main', __name__)

@main.route('/')
def home():
    page = request.args.get('page', type=int)
    dishes = Dish.query.order_by().paginate(page=page, per_page=5)
    return render_template('home.html', dishes=dishes)
