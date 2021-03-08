from flask import Blueprint, render_template, redirect, flash, request, url_for
from application.users.forms import LoginForm, RegistrationForm, UpdateProfileForm
from application import db, bcrypt
from application.models import User, Dish, Order
from flask_login import login_user, logout_user, current_user, login_required



users = Blueprint('users', __name__)

@users.route('/register', methods=['GET','POST'])
def register():
    if current_user.is_authenticated:
        return redirect('/')
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, email=form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash('Your account has been created! You can now login.', 'success')
        return redirect('/login')
    return render_template('register.html', title = 'Register', form=form)

@users.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect('/')
    form = LoginForm()
    if form.validate_on_submit():
        user=User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect('/')
        else:
            flash('Failed to log in. Please check email and password', 'danger')
    return render_template('login.html', title = 'Login', form=form)

@users.route('/logout')
def logout():
    logout_user()
    return redirect('/')

@users.route('/profile')
def profile():
    form = UpdateProfileForm()
    if form.validate_on_submit():
        current_user.username = form.username.data
        current_user.email = form.email.data
        db.session.commit()
        flash('Your profile has been updated', 'success')
        return redirect(url_for('users.profile'))
    elif request.method == 'GET':
        form.username.data = current_user.username
        form.email.data = current_user.email
    return render_template('profile.html', title='Profile', form=form)

@users.route('/orders/<string:user_id>')
def user_orders(user_id):
    user = User.query.filter_by(id = user_id).first_or_404()
    orders = Order.query.filter_by(user_id = user_id).all()
    dishes = []
    for order in orders:
        dish = Dish.query.filter_by(id = order.dish_id).all()
        dishes += dish
    return render_template('user_orders.html', dishes=dishes)