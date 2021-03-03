from flask_login import UserMixin, current_user
from application import db, login_manager
from flask_admin.contrib.sqla import ModelView
import os


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)

    def __repr__(self):
        return f"User('{self.username}', '{self.email}')"

class Dish(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), unique=True, nullable=False)
    price = db.Column(db.Float, nullable = False)
    picture = db.Column(db.String(20), nullable=False, default='default.jpg')
    cuisine = db.Column(db.String(30), unique=True, nullable=False)
    type = db.Column(db.String(20), nullable=False)

    def __repr__(self):
        return f"Dish('{self.name}', '{self.cuisine}', '{self.price}')"

class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    dish_id = db.Column(db.Integer, db.ForeignKey('dish.id'), nullable=False)
    quantity = db.Column(db.Integer, nullable=False, default=0)

    def __repr__(self):
        return f"Order('{self.user_id}', '{self.dish_id}', '{self.quantity}')"

class MyModelView(ModelView):
    def is_accessible(self):
        if current_user.email == os.getenv('ADMIN_USER1'):
            return current_user.is_authenticated        
        else:
            return False
