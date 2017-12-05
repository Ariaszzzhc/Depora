import datetime

from depora import db


class User(db.Model):
    # 表名
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(255))
    password = db.Column(db.String(255))

    articles = db.relationship(
        'Article',
        backref='users',
        lazy='dynamic'
    )

    def __init__(self, username):
        self.username = username

    def __repr__(self):
        """Define the string format for instance of User."""
        return "<Model User `{}`>".format(self.username)


articles_tags = db.Table('articles_tags',
                         db.Column('article_id', db.Integer, db.ForeignKey('articles.id')),
                         db.Column('tag_id', db.Integer, db.ForeignKey('tags.id'))
                         )


class Article(db.Model):
    __tablename__ = 'articles'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255))
    content = db.Column(db.String(255))
    publish = db.Column(db.DateTime)

    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    comments = db.relationship(
        'Comment',
        backref='articles',
        lazy='dynamic'
    )

    tags = db.relationship(
        'Tag',
        secondary=articles_tags,
        backref=db.backref('articles', lazy='dynamic'))

    def __init__(self, id, title, content):
        self.id = id
        self.title = title
        self.content = content
        self.publish = datetime.datetime.now()

    def __repr__(self):
        return "<Model Article `{}`>".format(self.title)


class Comment(db.Model):
    __tablename__ = 'comments'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    text = db.Column(db.Text())
    date = db.Column(db.DateTime())

    article_id = db.Column(db.Integer, db.ForeignKey('articles.id'))

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return '<Model Comment `{}`>'.format(self.name)


class Tag(db.Model):

    __tablename__ = 'tags'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return "<Model Tag `{}`>".format(self.name)
