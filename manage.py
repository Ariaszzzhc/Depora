import os

import click
from flask_migrate import Migrate

from depora import create_app
from depora.utils import db, bcrypt, login_manager
from depora.models import User, Article, Tag, Comment
from depora.configs import Config, DevConfig, ProdConfig
from depora.controller.home import home_blueprint
from depora.controller.article import article_blueprint
from depora.controller.admin import admin_blueprint
from depora.forms import LoginForm, ArticleForm

# 获取当前环境变量
# env = os.environ.get('ENV', 'dev')

app = create_app()

migrate = Migrate(app, db)


# 自定义命令
@app.cli.command
def init():
    click.echo('Initialize Database')
    db.create_all()


@app.shell_context_processor
def make_shell_context():
    return dict(app=app,
                db=db,
                bcrypt=bcrypt,
                login_manager=login_manager,
                home_blueprint=home_blueprint,
                admin_blueprint=admin_blueprint,
                article_blueprint=article_blueprint,
                Config=Config,
                DevConfig=DevConfig,
                ProdConfig=ProdConfig,
                LoginForm=LoginForm,
                ArticleForm=ArticleForm,
                User=User,
                Article=Article,
                Comment=Comment,
                Tag=Tag)


if __name__ == '__main__':
    app.run()
