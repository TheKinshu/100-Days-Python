import datetime
from flask import Flask, render_template, redirect, url_for
from flask.signals import request_finished
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from sqlalchemy.sql.schema import BLANK_SCHEMA
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, URL
from flask_ckeditor import CKEditor, CKEditorField
from datetime import date

## Delete this code:
# import requests
# posts = requests.get("https://api.npoint.io/43644ec4f0013682fc0d").json()

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
ckeditor = CKEditor(app)
Bootstrap(app)

##CONNECT TO DB
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///posts.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

##CONFIGURE TABLE
class BlogPost(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    subtitle = db.Column(db.String(250), nullable=False)
    date = db.Column(db.String(250), nullable=False)
    body = db.Column(db.Text, nullable=False)
    author = db.Column(db.String(250), nullable=False)
    img_url = db.Column(db.String(250), nullable=False)


##WTForm
class CreatePostForm(FlaskForm):
    title = StringField("Blog Post Title", validators=[DataRequired()])
    subtitle = StringField("Subtitle", validators=[DataRequired()])
    author = StringField("Your Name", validators=[DataRequired()])
    img_url = StringField("Blog Image URL", validators=[DataRequired(), URL()])
    body = CKEditorField("Blog Content", validators=[DataRequired()])
    submit = SubmitField("Submit Post")


##RENDER HOME PAGE USING DB
@app.route('/')
def get_all_posts():
    posts = BlogPost.query.all()
    return render_template("index.html", all_posts=posts)


##RENDER POST USING DB
@app.route("/post/<int:post_id>")
def show_post(post_id):
    requested_post = BlogPost.query.get(post_id)
    return render_template("post.html", post=requested_post)


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/edit-post/<int:post_id>", methods=["GET", "POST"])
def edit_post(post_id):
    blog = BlogPost.query.get(post_id)
    form = CreatePostForm(
        title = blog.title,
        subtitle = blog.subtitle,
        author = blog.author,
        img_url = blog.img_url,
        body = blog.body
    )
    if form.validate_on_submit():
        blog.title = form.title.data
        blog.subtitle = form.subtitle.data
        blog.author = form.author.data
        blog.img_url = form.img_url.data
        blog.body = form.body.data
        db.session.commit()
        return redirect(url_for("get_all_posts"))
    return render_template("make-post.html", form=form, edit=True)

@app.route("/new-post", methods=["GET", "POST"])
def new_post():
    form = CreatePostForm()
    if form.validate_on_submit():
        blog = BlogPost(
            title = form.title.data,
            subtitle = form.subtitle.data,
            date = date.today().strftime("%B %d, %Y"),
            body = form.body.data,
            author = form.author.data,
            img_url = form.img_url.data
        )
        db.session.add(blog)
        db.session.commit()
        return redirect(url_for("get_all_posts"))
    return render_template("make-post.html", form=form, edit=False)

@app.route("/delete/<post_id>")
def delete_post(post_id):
    blog = BlogPost.query.get(post_id)
    db.session.delete(blog)
    db.session.commit()
    return redirect(url_for("get_all_posts"))
    pass
if __name__ == "__main__":
    app.run(debug=True)