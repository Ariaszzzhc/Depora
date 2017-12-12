from os import path
from flask import render_template, Blueprint, redirect, url_for
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
    if not path.exists('config.json'):
        return redirect(url_for('home.install'))

    try:
        article = Article.query.get_or_404(id)
        return render_template('article.html', article=article)
    except NotFound:
        return render_template('404.html')
