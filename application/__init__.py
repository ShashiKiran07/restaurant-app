from application.config import Config
from flask import Flask
from application.config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_bcrypt import Bcrypt
from flask_admin import Admin


db = SQLAlchemy()
login_manager = LoginManager()
bcrypt = Bcrypt()
admin = Admin()
login_manager.login_view = 'users.login'
login_manager.login_message_category = 'info'



def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    with app.app_context():
        db.create_all()

    login_manager.init_app(app)
    bcrypt.init_app(app)
    admin.init_app(app)

    from application.models import User, Dish, Order, MyModelView
    admin.add_view(MyModelView(User, db.session))
    admin.add_view(MyModelView(Dish, db.session))
    admin.add_view(MyModelView(Order, db.session))

    from application.users.routes import users
    from application.main.routes import main
    from application.errors.handlers import errors


    app.register_blueprint(users)
    app.register_blueprint(main)
    app.register_blueprint(errors)



    return app
