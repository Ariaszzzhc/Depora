from flask import Flask
from flaskext.markdown import Markdown

from depora import configs
from depora.utils import db, bcrypt
from depora.controller.admin import admin_blueprint
from depora.controller.article import article_blueprint
from depora.controller.home import home_blueprint


def create_app(config):
    app = Flask(__name__)
    app.config.from_object(config)

    db.init_app(app)
    bcrypt.init_app(app)
    Markdown(app)

    app.register_blueprint(admin_blueprint)
    app.register_blueprint(article_blueprint)
    app.register_blueprint(home_blueprint)

    return app
