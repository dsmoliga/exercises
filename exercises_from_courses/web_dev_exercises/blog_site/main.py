from flask import Flask, render_template
from post import Post
import requests

blog_posts = requests.get("https://api.npoint.io/c790b4d5cab58020d391").json()
post_objects = []
for post in blog_posts:
    post_obj = Post(post["id"], post["title"], post["subtitle"], post["body"])
    post_objects.append(post_obj)


app = Flask(__name__)


@app.route('/')
def home():
    return render_template("index.html", all_posts=post_objects)


@app.route('/post/<int:index>')
def show_post(index):
    requested_post = list(filter(lambda post: post.id == index, post_objects))
    return render_template('post.html', post=requested_post[0])


if __name__ == "__main__":
    app.run(debug=True)
