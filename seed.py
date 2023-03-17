from models import User, db
from app import app

# to run this, just $ python seed.py

db.drop_all()
db.create_all()

u1 = User(first_name = "Bjorn", last_name = "Nitmo", image_url="https://cdn.pixabay.com/photo/2016/02/11/16/59/dog-1194083_960_720.jpg")
u2 = User(first_name = "Marie", last_name = "Jansen", image_url="https://cdn.pixabay.com/photo/2016/02/11/16/59/dog-1194083_960_720.jpg")
u3 = User(first_name = "Orval", last_name = "Auteberry", image_url="https://cdn.pixabay.com/photo/2016/02/11/16/59/dog-1194083_960_720.jpg")
u4 = User(first_name = "Isabel", last_name = "Dobbs", image_url="https://cdn.pixabay.com/photo/2016/02/11/16/59/dog-1194083_960_720.jpg")
u5 = User(first_name = "Arti", last_name = "Wheelock", image_url="https://cdn.pixabay.com/photo/2016/02/11/16/59/dog-1194083_960_720.jpg")
u6 = User(first_name = "Dan", last_name = "Collins", image_url="https://cdn.pixabay.com/photo/2016/02/11/16/59/dog-1194083_960_720.jpg")

db.session.add(u1)
db.session.add(u2)
db.session.add(u3)
db.session.add(u4)
db.session.add(u5)
db.session.add(u6)
db.session.commit()
