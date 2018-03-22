from os import path
from flask import Blueprint


article_blueprint = Blueprint(
    'article',
    __name__,
    url_prefix='/index',
    template_folder=path.join(path.pardir, "templates", "install")
)



