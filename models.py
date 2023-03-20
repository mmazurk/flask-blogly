"""models for Blogly project"""

from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

# creates the new SQLAlchemy object to work with
db = SQLAlchemy()

def connect_db(app):
    """Set up a connection between a Flask application and a database."""

    # sets the flask instance to the object's "app" attribute
    # and therefore makes the SQLA object aware of the app
    db.app = app

    # initializes the SQLA object with flask application instance
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


class Post(db.Model):

    __tablename__ = "posts"

    post_id = db.Column(db.Integer,
                        primary_key=True,
                        autoincrement=True)
    title = db.Column(db.String(25),
                      nullable=False)
    content = db.Column(db.String(280),
                        nullable=False)
    created_at = db.Column(db.DateTime(),
                           default = datetime.utcnow,
                           nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('blogly_users.user_id'))
    
    user = db.relationship('User', backref='posts')

    tags = db.relationship("PostTag", backref = 'post')

    def __repr__(self):
        """show info about posts"""
        s = self
        return f"<Post {s.title} {s.content} {s.created_at}>"


class PostTag(db.Model):

    __tablename__ = "posts_tags"

    post_id = db.Column(db.Integer, db.ForeignKey('posts.post_id'),
                        primary_key = True)
    tag_id = db.Column(db.Integer, db.ForeignKey('tags.tag_id'),
                       primary_key = True)


class Tag(db.Model):

    __tablename__ = "tags"

    tag_id = db.Column(db.Integer,
                       primary_key = True,
                       autoincrement = True)
    name = db.Column(db.String(20),
                     nullable = False,
                     unique = True)
    
    posts = db.relationship("PostTag", backref = 'tag')