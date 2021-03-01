from flask_login import UserMixin, current_user
from application import login_manager, db
import os

class User(db.model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)

    def __repr__(self):
        return f"User('{self.username}', '{self.email}')"

class Dish(db.model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), unique=True, nullable=False)
    price = db.Column(db.Float, nullable = False)
    picture = db.Column(db.String(20), nullable=False, default='default.jpg')
    cuisine = db.Column(db.String(30), unique=True, nullable=False)