""" Models for adopt pet app """

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

PLACEHOLDER_PHOTO = "https://bit.ly/31YSHxD"

def connect_db(app):
    """ Connect to database """
    db.app = app
    db.init_app(app)


class Pet(db.Model):
    """ Model for pets data table """

    __tablename__ = "pets"

    id = db.Column(db.Integer,
        primary_key=True,
        autoincrement=True)
    name = db.Column(db.String(50),
        nullable=False)
    species = db.Column(db.String(50),
        nullable=False)
    photo_url = db.Column(db.Text,
        nullable=False,
        default = PLACEHOLDER_PHOTO)
    age = db.Column(db.Integer,
        nullable=False)
    notes = db.Column(db.Text,
        nullable=False)
    available = db.Column(db.Boolean,
        nullable=False,
        default=True)

    def __repr__(self):
        return f'<Pet id: {self.id}, name: {self.name}, available: {self.available}>'
