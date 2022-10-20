"""Models for Cupcake app."""

from flask_sqlalchemy import SQLAlchemy
from traitlets import default

db = SQLAlchemy()


def connect_db(app):
    """Connect to database."""
    with app.app_context():
        db.app = app
        db.init_app(app)


class Cupcake(db.Model):
    """Cupcakes."""

    __tablename__ = "cupcake"

    @property
    def to_dict(self):
        return {
            "id" : self.id,
            "flavor" : self.flavor,
            "size" : self.size,
            "rating" : self.rating,
            "image" : self.image
        }

    default_img = "https://tinyurl.com/demo-cupcake"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    flavor = db.Column(db.Text, nullable=False)
    size = db.Column(db.Text, nullable=False)
    rating = db.Column(db.Float, nullable=False)
    image = db.Column(db.Text, nullable=False, default=default_img)

  
