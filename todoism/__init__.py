import os
from flask import Flask

from todoism.blueprints.home import home_bp
from todoism.settings import config
from todoism.extensions import db, migrate
from todoism.models import User, Item

def create_app(config_name=None):
    if config_name is None:
        config_name = os.getenv('FLASK_CONFIG', 'development')
    
    app = Flask('todoism')
    app.config.from_object(config[config_name])

    register_blueprints(app)
    register_extensions(app)

    return app


def register_blueprints(app):
    app.register_blueprint(home_bp)


def register_extensions(app):
    db.init_app(app)
    migrate.init_app(app, db)