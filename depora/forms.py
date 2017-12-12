from flask_wtf import FlaskForm
from wtforms import (
    StringField,
    TextField,
    TextAreaField,
    PasswordField,
    BooleanField,
    ValidationError
)
from wtforms.validators import DataRequired, Length, EqualTo, URL

from depora.models import User


class LoginForm(FlaskForm):
    username = StringField('Username', [DataRequired(), Length(max=255)])
    password = StringField('Password', [DataRequired()])
    remember = BooleanField('Remember Me')

    def validate(self):
        check_validata = super(LoginForm, self).validate()

        if not check_validata:
            return False

        user = User.query.filter_by(username=self.username.data).first()

        if not user:
            self.username.errors.append('Invalid username or password.')
            return False

        if not user.check_password(self.password.data):
            self.username.errors.append('Invalid username or password.')
            return False

        return True


class ArticleForm(FlaskForm):
    title = StringField('Title', [DataRequired(), Length(max=255)])
    text = TextAreaField('Blog Content', [DataRequired()])


class InstallForm(FlaskForm):
    blog_name = StringField('Blog Name', [DataRequired()])
    database_name = StringField('Database Name', [DataRequired()])
    database_username = StringField('Database Name', [DataRequired()])
    database_password = StringField('Database Password', [DataRequired()])
    database_address = StringField('Database Address', [DataRequired()])
