import os

from flask_script import Manager, Server
from flask_migrate import Migrate, MigrateCommand

from depora import create_app
from depora.utils import db
from depora.models import User, Article, Tag, Comment

# 获取当前环境变量
env = os.environ.get('ENV', 'dev')

app = create_app('depora.configs.%sConfig' % env.capitalize())

manager = Manager(app)

migrate = Migrate(app, db)

manager.add_command("server", Server())
manager.add_command("migrate", MigrateCommand)


@manager.shell
def make_shell_context():
    return dict(app=app,
                db=db,
                User=User,
                Article=Article,
                Comment=Comment,
                Tag=Tag)


if __name__ == '__main__':
    manager.run()
