from flask import Flask, request, redirect, render_template
from models import db, connect_db, User

app = Flask(__name__)
# app.app_context().push() 
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///blogly'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True

from flask_debugtoolbar import DebugToolbarExtension
app.config['SECRET_KEY'] = "SECRET!"
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
debug = DebugToolbarExtension(app)

connect_db(app)
with app.app_context(): # Ask Zak about having to add this
    db.create_all()

@app.route("/")
def redirect_users():
    """Redirect to list of users"""
    return redirect("/users")

@app.route("/users")
def list_users():
    """List users and show add form."""

    users = User.query.all()
    return render_template("users.html", users = users)

@app.route("/users/new")
def create_user():
    """List users and show add form."""

    return render_template("create-user.html")

@app.route("/users/new", methods=['POST'])
def process_post():
    """process form data"""
    