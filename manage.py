import click

from depora import create_app
from depora.utils import mongo

app = create_app()


@app.shell_context_processor
def make_shell_context():
    return dict(app=app,
                mongo=mongo)


if __name__ == '__main__':
    app.run()
