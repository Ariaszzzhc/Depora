from os import path
from flask import Flask
from flaskext.markdown import Markdown

from depora import configs
from depora.utils import db, bcrypt, login_manager
from depora.controller.admin import admin_blueprint
from depora.controller.article import article_blueprint
from depora.controller.home import home_blueprint


def create_app():
    app = Flask(__name__)
    if path.exists('config.json'):
        app.config.from_json('../config.json')
    else:
        app.config['WTF_CSRF_ENABLED'] = False
        app.config['DEBUG'] = True

    db.init_app(app)
    bcrypt.init_app(app)
    login_manager.init_app(app)
    Markdown(app)

    app.register_blueprint(admin_blueprint)
    app.register_blueprint(article_blueprint)
    app.register_blueprint(home_blueprint)

    return app
