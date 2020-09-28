from app.models import Post
from app import db

all_posts = Post.query.filter()
#print(all_posts)

all_posts2 = all_posts.order_by(Post.timestamp.desc())
#print(all_posts2)

all_posts3 = Post.query.order_by(Post.timestamp.desc())
print(all_posts3.all())
