from .. import db


class Configuration(db.Model):
    __tablename__ = "configuration"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    key = db.Column(db.String(255), nullable=False)
    value = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return "<Configuration '{}'>".format(self.key)
