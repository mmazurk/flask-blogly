from flask import Flask, request, redirect, render_template
from models import db, connect_db, User, Post, PostTag, Tag
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
    posts = User.query.get(user_id).posts
    return render_template("detail-page.html", user = user, posts = posts)

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

@app.route("/users/<int:user_id>/posts/new")
def add_post(user_id):
    """Delete a user"""
    
    user = User.query.get_or_404(user_id)
    # posts = User.query.get(user_id).posts
    return render_template("create-post.html", user = user)

### =========================================================================

@app.route("/users/<int:user_id>/posts/new", methods = ['POST'])
def process_new_post(user_id):
    """Delete a user"""
    
    # get the form data
    title = request.form["post-title"]
    content = request.form["post-content"]

    # update the database    
    user = User.query.get_or_404(user_id)
    post = Post(title = title, content = content, user_id = user.user_id)
    db.session.add(post)
    db.session.commit()

    # redirect the user       
    return redirect("/users")

@app.route("/posts/<int:post_id>")
def show_post(post_id):
    """Delete a user"""
    
    post = Post.query.get_or_404(post_id)
           
    return render_template("show-post.html", post = post)

###################################################################################

### TODO: (routes)

# GET /posts/[post-id]/edit
# Show form to edit a post, and to cancel (back to user page).

# POST /posts/[post-id]/edit
# Handle editing of a post. Redirect back to the post view.

# POST /posts/[post-id]/delete
# Delete the post.

### TODO: (user interface)

# Create user interface
# Add Tag
# Edit Tag
# List Tags
# Show Tag
# Show Post with Tags
# Add Post with Tags
# Edit Post with Tags

### TODO: (routes)

# GET /tags
# Lists all tags, with links to the tag detail page.

# GET /tags/[tag-id]
# Show detail about a tag. Have links to edit form and to delete.

# GET /tags/new
# Shows a form to add a new tag.

# POST /tags/new
# Process add form, adds tag, and redirect to tag list.

# GET /tags/[tag-id]/edit
# Show edit form for a tag.

# POST /tags/[tag-id]/edit
# Process edit form, edit tag, and redirects to the tags list.

# POST /tags/[tag-id]/delete
# Delete a tag.