from models import User, Post, Tag, PostTag, db
from app import app

# to run this, just $ python seed.py

db.drop_all()
db.create_all()

u1 = User(first_name = "Bjorn", last_name = "Nitmo", image_url="https://cdn.pixabay.com/photo/2022/12/02/05/13/dog-7630252_960_720.jpg")
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

p1 = Post(title = "Any delicate", content = "Any delicate you how kindness horrible outlived servants. You high bed wish help call draw side. Girl quit if case mr sing as no have. At none neat am do over will.", user_id = 1)
p2 = Post(title = "Dashwood contempt", content = "Dashwood contempt on mr unlocked resolved provided of of. Stanhill wondered it it welcomed oh. Hundred no prudent he however smiling at an offence.", user_id = 1)
p3 = Post(title = "Neat own", content = "Neat own nor she said see walk. And charm add green you these. Sang busy in this drew ye fine. At greater prepare musical so attacks as on distant. ", user_id = 2)
p4 = Post(title = "To shewing", content = "To shewing another demands to. Marianne property cheerful informed at striking at. Clothes parlors however by cottage on. In views it or meant drift to.", user_id = 2)
p5 = Post(title = "If wandered", content = "If wandered relation no surprise of screened doubtful. Overcame no insisted ye of trifling husbands. Might am order hours on found.", user_id = 3)
p6 = Post(title = "Subjects to", content = "Subjects to ecstatic children he. Could ye leave up as built match. Dejection agreeable attention set suspected led offending.", user_id = 3)
p7 = Post(title = "New had happen", content = "New had happen unable uneasy. Drawings can followed improved out sociable not. Earnestly so do instantly pretended. ", user_id = 4)
p8 = Post(title = "Acceptance middletons", content = "Acceptance middletons me if discretion boisterous travelling an. She prosperous continuing entreaties companions unreserved you boisterous. ", user_id = 4)
p9 = Post(title = "Ham followed", content = "Ham followed now ecstatic use speaking exercise may repeated. Himself he evident oh greatly my on inhabit general concern. ", user_id = 5)
p10 = Post(title = "Neat own nor", content = "Neat own nor she said see walk. And charm add green you these. Sang busy in this drew ye fine. At greater prepare musical so attacks as on distant.", user_id = 5)
p11 = Post(title = "Received the likewise", content = "Received the likewise law graceful his. Nor might set along charm now equal green. Pleased yet equally correct colonel not one.", user_id = 6)

posts = [p1, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11]
db.session.add_all(posts)
db.session.commit()

t1 = Tag(name = "Fun")
t2 = Tag(name = "LULZ")
t3 = Tag(name = "Sad")
t4 = Tag(name = "Not extreme, dude")
t5 = Tag(name = "Like whatever")
t6 = Tag(name = "Ummm")

tag_posts = [t1, t2, t3, t4, t5, t6]
db.session.add_all(tag_posts)
db.session.commit()

pt1 = PostTag(post_id = 1, tag_id = 1)
pt2 = PostTag(post_id = 2, tag_id = 2)
pt3 = PostTag(post_id = 3, tag_id = 3)
pt4 = PostTag(post_id = 4, tag_id = 3)
pt5 = PostTag(post_id = 5, tag_id = 4)
pt6 = PostTag(post_id = 5, tag_id = 5)

pt_posts = [pt1, pt2, pt3, pt4, pt5, pt6]
db.session.add_all(pt_posts)
db.session.commit()
