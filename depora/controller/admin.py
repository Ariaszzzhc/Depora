from os import path
from flask import render_template, Blueprint, redirect
from flask_login import login_required

from depora.models import db, Article
from depora.forms import ArticleForm

admin_blueprint = Blueprint(
    'admin',
    __name__,
    template_folder=path.join(path.pardir, 'templates', 'admin'),
    url_prefix='/admin'
)


@admin_blueprint.route('/write', methods=['GET', 'POST'])
@login_required
def new_article():
    form = ArticleForm()

    if form.validate_on_submit():
        article = Article(title=form.title.data, content=form.text.data)

        db.session.add(article)
        db.session.commit()
        return redirect('/admin')

    return render_template('admin/write.html',
                           form=form)


@admin_blueprint.route('/')
@login_required
def admin():
    articles = Article.query.all()
    return render_template('admin/index.html', articles=articles)


@admin_blueprint.route('/delete/<id>')
def delete(id):
    Article.query.filter_by(id=id).delete()
    db.session.commit()

    return redirect('/admin')


@admin_blueprint.route('/update/<id>', methods=['GET', 'POST'])
@login_required
def update(id):
    article = Article.query.filter_by(id=id).first()
    form = ArticleForm()
    form.title.data = article.title
    form.text.data = article.content

    if form.validate_on_submit():
        article.title = form.title.data
        article.content = form.text.data

        db.session.commit()
        return redirect('/admin')

    return render_template('admin/update.html', form=form, id=article.id)
