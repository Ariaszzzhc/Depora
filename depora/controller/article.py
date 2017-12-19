from os import path
from flask import render_template, Blueprint, redirect, url_for
from werkzeug.exceptions import NotFound

from depora.models import Article, Option

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

    site_description = Option.query.filter_by(key='siteDescription').first()
    site_name = Option.query.filter_by(key='siteName').first()

    try:
        article = Article.query.get_or_404(id)
        title = article.title
        return render_template(
            'article.html',
            article=article,
            title=title,
            site_name=site_name,
            site_description=site_description
        )
    except NotFound:
        title = '404'
        return render_template(
            '404.html',
            title=title,
            site_name=site_name,
            site_description=site_description
        )
