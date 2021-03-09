from flask import Blueprint, render_template, redirect, flash, request, url_for
from application.main.forms import OrderForm
from application import db, bcrypt
from application.models import User, Dish, Order
from flask_login import login_user, logout_user, current_user, login_required


main = Blueprint('main', __name__)

@main.route('/', methods = ['GET', 'POST'])
def home():
    dishes = Dish.query.all()
    form = OrderForm()
    if current_user.is_authenticated:
        for dish in dishes:
            if form.validate_on_submit():
                order = Order(user_id = current_user.id, dish_id = dish.id, quantity = form.quantity.data)
                db.session.add(order)
                db.session.commit()
                flash('Your Order has been placed', 'success')
                return redirect(url_for('users.user_orders'))
    return render_template('home.html', dishes=dishes, form=form)