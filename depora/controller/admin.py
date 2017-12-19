from os import path
from flask import render_template, Blueprint, redirect, request, url_for
from flask_login import login_required, logout_user

from depora.models import db, Article, Option, User
from depora.forms import ArticleForm, OptionForm

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

        article.user_id = User.query.filter_by(id=1).first().id
        db.session.add(article)
        db.session.commit()
        return redirect('/admin')

    return render_template('admin/write.html',
                           form=form)


@admin_blueprint.route('/')
@login_required
def admin():
    # articles = Article.query.all()
    count = Article.query.count()
    recents = Article.query.order_by(Article.publish.desc()).limit(5).all()

    return render_template('admin/index.html', count=count, recents=recents)


@admin_blueprint.route('/delete/<id>')
@login_required
def delete(id):
    Article.query.filter_by(id=id).delete()
    db.session.commit()

    return redirect('/admin')


@admin_blueprint.route('/update/<id>', methods=['GET', 'POST'])
@login_required
def update(id):
    article = Article.query.filter_by(id=id).first()
    form = ArticleForm()

    if request.method == 'GET':
        form.title.data = article.title
        form.text.data = article.content

    if form.validate_on_submit():
        article.title = form.title.data
        article.content = form.text.data

        db.session.commit()
        return redirect('/admin')

    return render_template('admin/write.html', form=form, id=article.id)


@admin_blueprint.route('/manage')
@login_required
def manage():
    page = request.args.get('page', 1, type=int)
    pagination = Article.query.order_by(Article.id) \
        .paginate(page, per_page=20, error_out=False)

    articles = pagination.items

    return render_template('admin/manage.html', articles=articles, pagination=pagination)


@admin_blueprint.route('/logout')
@login_required
def logout():
    logout_user()
    return render_template('admin/logout.html')


@admin_blueprint.route('/option', methods=['GET', 'POST'])
@login_required
def option():
    site_name = Option.query.filter_by(key='siteName').first()
    site_url = Option.query.filter_by(key='siteUrl').first()
    site_description = Option.query.filter_by(key='siteDescription').first()
    form = OptionForm()

    if request.method == 'GET':
        form.site_name.data = site_name.value
        form.site_url.data = site_url.value
        form.site_description.data = site_description.value

    if form.validate_on_submit():
        site_name.value = form.site_name.data
        site_url.value = form.site_url.data
        site_description.value = form.site_description.data

        db.session.commit()

        return redirect(url_for('admin.admin'))

    return render_template('admin/option.html', form=form)
