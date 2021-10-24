from main import db
from main import Post

db.create_all()

first = Post(title="First",content="Sarasa sasa")

db.session.add(first)
db.session.commit()