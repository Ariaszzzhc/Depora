from flask import render_template

from depora import app
from depora.models import Article, Comment, Tag, User


@app.route('/')
def index():
    articles = Article.query.all()
    return render_template('index.html', articles=articles)
