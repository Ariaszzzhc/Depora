from os import path
from flask import render_template, Blueprint, request, flash, redirect

from depora.models import Article
from depora.forms import LoginForm

home_blueprint = Blueprint(
    'home',
    __name__,
    template_folder=path.join(path.pardir, 'templates'),
    url_prefix='/'
)

site_description = '''
Hello, Depora!
'''


@home_blueprint.route('/')
def index():
    page = request.args.get('page', 1, type=int)
    pagination = Article.query.order_by(Article.publish.desc())\
        .paginate(page, per_page=10, error_out=False)
    articles = pagination.items
    return render_template('index.html', articles=articles, site_description=site_description, pagination=pagination)


@home_blueprint.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()

    if form.validate_on_submit():
        flash("登陆成功", category="success")

        return redirect('/admin')

    return render_template('admin/login.html', form=form)
