from flask import render_template, redirect, request
from werkzeug.exceptions import NotFound

from depora import app, db
from depora.models import Article, Comment, Tag, User
from depora.forms import ArticleForm

site_description = '''
Hello, Depora!
'''


@app.route('/')
def index():
    page = request.args.get('page', 1, type=int)
    pagination = Article.query.order_by(Article.publish.desc())\
        .paginate(page, per_page=10, error_out=False)
    articles = pagination.items
    return render_template('index.html', articles=articles, site_description=site_description, pagination=pagination)


@app.route('/article/<id>')
def article(id):
    try:
        article = Article.query.get_or_404(id)
        return render_template('article.html', article=article)
    except NotFound:
        return render_template('404.html')


@app.route('/admin/write', methods=['GET', 'POST'])
def new_article():
    form = ArticleForm()

    if form.validate_on_submit():
        article = Article(title=form.title.data, content=form.text.data)

        db.session.add(article)
        db.session.commit()
        return redirect('/admin')

    return render_template('admin/write.html',
                           form=form)


@app.route('/admin')
def admin():
    articles = Article.query.all()
    return render_template('admin/index.html', articles=articles)


@app.route('/admin/delete/<id>')
def delete(id):
    Article.query.filter_by(id=id).delete()
    db.session.commit()

    return redirect('/admin')


@app.route('/admin/update/<id>', methods=['GET', 'POST'])
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
