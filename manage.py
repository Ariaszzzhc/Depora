from flask_script import Manager, Server
from flask_migrate import Migrate, MigrateCommand

from depora import app, db, models

manager = Manager(app)

migrate = Migrate(app, db)

manager.add_command("server", Server())
manager.add_command("migrate", MigrateCommand)


@manager.shell
def make_shell_context():
    return dict(app=app,
                db=db,
                User=models.User,
                Article=models.Article,
                Comment=models.Comment,
                Tag=models.Tag)


if __name__ == '__main__':
    manager.run()
