from application.config import Config
from flask import Flask
from application.config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_bcrypt import Bcrypt


db = SQLAlchemy()
login_manager = LoginManager()
bcrypt = Bcrypt()


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    with app.app_context():
        db.create_all()

    login_manager.init_app(app)
    bcrypt.init_app(app)
    from application.users.routes import users
    from application.main.routes import main
    app.register_blueprint(users)
    app.register_blueprint(main)


    return app
