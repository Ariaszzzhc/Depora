from flask import Flask

from .configs import Config
from .utils import mongo
from .controller.article import article_blueprint


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    mongo.init_app(app)

    app.register_blueprint(article_blueprint)

    return app
