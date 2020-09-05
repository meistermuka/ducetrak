import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from config import Config


def create_app():

    app = Flask(__name__)
    app.config.from_object(Config)
    # db = SQLAlchemy(app)
    # migrate = Migrate(app, db)

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    return app
