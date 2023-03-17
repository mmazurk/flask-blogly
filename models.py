"""models for Blogly project"""

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def connect_db(app):
    """Connect to database."""
    db.app = app
    db.init_app(app)

class User(db.Model):
    """Represents a User in our Blogly app"""

    __tablename__ = "blogly_users"

    user_id = db.Column(db.Integer,
                        primary_key=True,
                        autoincrement=True)
    first_name = db.Column(db.String(20),
                           nullable=False)
    last_name = db.Column(db.String(25),
                          nullable=False)
    image_url = db.Column(db.String(200),
                          nullable=False,
                          default="https://cdn.pixabay.com/photo/2023/03/09/20/02/cat-7840767_960_720.jpg")
    
    def __repr__(self):
        """show info about users"""
        s = self
        return f"<User {s.first_name} {s.last_name} {s.image_url}>"
    
    @classmethod
    def get_all(cls):
        """Get all data"""
        return cls.query.all()
    

