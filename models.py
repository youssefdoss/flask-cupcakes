"""Models for Cupcake app."""

from flask import request
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def connect_db(app):
    """Connect to database."""

    app.app_context().push()
    db.app = app
    db.init_app(app)

class Cupcake(db.Model):
    '''Cupcake.'''

    __tablename__ = 'cupcakes'

    id = db.Column(
        db.Integer,
        primary_key=True,
        autoincrement=True,
    )

    flavor = db.Column(
        db.Text,
        nullable=False
    )

    size = db.Column(
        db.Text,
        nullable=False
    )

    rating = db.Column(
        db.Integer,
        nullable=False
    )

    image = db.Column(
        db.Text,
        nullable=False,
        default='https://tinyurl.com/demo-cupcake' # Make it a global constant
    )

    def serialize(self):
        '''Serialize to dictionary'''

        return {
            "id": self.id,
            "flavor": self.flavor,
            "size": self.size,
            "rating": self.rating,
            "image": self.image
        }

    def check_if_none_and_update(self):
        '''Checks which values are passed into the request and update accordingly'''
            
        self.flavor = request.json.get('flavor', self.flavor)
        self.size = request.json.get('size', self.size)
        self.rating = request.json.get('rating', self.rating)
        self.image = request.json.get('image', self.image)