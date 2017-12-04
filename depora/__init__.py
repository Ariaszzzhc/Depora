from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from depora import configs

app = Flask(__name__)
app.config.from_object(configs.DevConfig)
db = SQLAlchemy(app)

__import__('depora.views')