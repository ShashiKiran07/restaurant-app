from application.config import Config
from flask import Flask
from application.config import Config
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    from application.users.routes import users
    app.register_blueprint(users)


    return app