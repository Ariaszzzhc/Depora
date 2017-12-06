from os import path
from flask import render_template, Blueprint
from werkzeug.exceptions import NotFound

from depora.models import Article

article_blueprint = Blueprint(
    'article',
    __name__,
    template_folder=path.join(path.pardir, 'templates'),
    url_prefix='/article'
)


@article_blueprint.route('/<id>')
def article(id):
    try:
        article = Article.query.get_or_404(id)
        return render_template('article.html', article=article)
    except NotFound:
        return render_template('404.html')
