from flask_script import Manager, Server

from depora import app, db, models

manager = Manager(app)
manager.add_command("server", Server())


@manager.shell
def make_shell_context():
    return dict(app=app,
                db=db,
                user=models.User)


if __name__ == '__main__':
    manager.run()
