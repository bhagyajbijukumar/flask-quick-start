from flask import Flask

from blueprints.admin import admin
from blueprints.user import user

from extensions import db, csrf


def create_app(config_file):
    app = Flask(__name__)
    app.config.from_pyfile(config_file)
    
    db.init_app(app)
    csrf.init_app(app)

    app.register_blueprint(admin)
    app.register_blueprint(user)


    return app