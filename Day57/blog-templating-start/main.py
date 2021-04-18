from flask import Flask, render_template
from post import Post
import requests

app = Flask(__name__)

blog_post = []

blog_api = "https://api.npoint.io/5abcca6f4e39b4955965"
response = requests.get(blog_api)
response.raise_for_status()
for blog in response.json():
    obj = Post(blog['id'], blog['title'], blog['subtitle'], blog['body'])
    blog_post.append(obj)


@app.route('/')
def home():
    return render_template("index.html", blogs=blog_post)

@app.route('/post/<int:id>')
def more_blog(id):
    return render_template("post.html", blog=blog_post[id])

if __name__ == "__main__":
    app.run(debug=True)
