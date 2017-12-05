from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt

from depora import configs

app = Flask(__name__)
app.config.from_object(configs.DevConfig)
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)

__import__('depora.views')