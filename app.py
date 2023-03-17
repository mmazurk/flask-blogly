from flask import Flask, request, redirect, render_template
from models import db, connect_db, User
from flask_debugtoolbar import DebugToolbarExtension

app = Flask(__name__)
app.app_context().push() 
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///blogly'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['SECRET_KEY'] = "SECRET!"
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
debug = DebugToolbarExtension(app)

connect_db(app)
db.create_all() 

# For testing
 # https://cdn.pixabay.com/photo/2023/03/12/17/35/hare-7847442_960_720.jpg  
# https://cdn.pixabay.com/photo/2022/12/02/05/13/dog-7630252_960_720.jpg

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
 
    first_name = request.form["first-name"]
    last_name = request.form["last-name"]
    image = request.form["image-url"]
    new_user = User(first_name = first_name, last_name = last_name, image_url= image)
    db.session.add(new_user)
    db.session.commit()
    return redirect("/users")

@app.route("/users/<int:user_id>")
def show_details(user_id):
    """show user detail page"""

    user = User.query.get_or_404(user_id)
    return render_template("detail-page.html", user = user)

@app.route("/users/<int:user_id>/edit")
def edit_details(user_id):
    """Edit user"""

    user = User.query.get_or_404(user_id)
    return render_template("edit-user.html", user = user)

@app.route("/users/<int:user_id>/edit", methods = ['POST'])
def edit_user(user_id):
    """Process posted user edit"""

    user = User.query.get_or_404(user_id)
    
    if request.form["first-name"]:
        user.first_name = request.form["first-name"]
    if request.form["last-name"]:
        user.last_name = request.form["last-name"]
    if request.form["image-url"]:
        user.image_url = request.form["image-url"]

    db.session.add(user)
    db.session.commit()
    return redirect("/users")

@app.route("/users/<int:user_id>/delete")
def delete_user(user_id):
    """Delete a user"""
    
    user = User.query.get_or_404(user_id)
    User.query.filter_by(user_id = user.user_id).delete()
    db.session.commit()
       
    return redirect("/users")