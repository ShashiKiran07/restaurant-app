from application.models import Dish
from flask import Blueprint, render_template, redirect, flash, request
from application.models import Dish
from application.main.forms import TypeForm


main = Blueprint('main', __name__)

@main.route('/')
def home():
    page = request.args.get('page', type=int)
    dishes = Dish.query.order_by().paginate(page=page, per_page=5)
    return render_template('home.html', dishes=dishes)

@main.route('/', methods = ['GET', 'POST'])
def choice():
    form = TypeForm()
    if form.validate_on_submit():
        type = form.type.data
        return render_template('home.html', form=form)
