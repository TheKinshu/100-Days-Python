from flask import Flask, render_template, redirect, url_for, request
from flask.wrappers import Response
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from sqlalchemy.orm import query
from wtforms import StringField, SubmitField
from wtforms.fields.core import FloatField, IntegerField
from wtforms.validators import DataRequired
import requests
from pprint import pprint

MOVIE_API_KEY = "1f2d84049fe6d4cb12778c028ee992ba"
themoviedb_endpoint = "https://api.themoviedb.org/3/search/movie"
movieDetail_endpoint = "https://api.themoviedb.org/3/movie/"

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap(app)

app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///movie-ranking.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Find Movie
class GetMovieForm(FlaskForm):
    title = StringField('Movie Title', validators=[DataRequired()])
    submit = SubmitField('Add Movie')

# Flask form
class MovieForm(FlaskForm):
    rating = FloatField('Your Rating Out of 10 e.g. 7.5')
    review = StringField('Your Review')
    submit = SubmitField('Done')


# Creating Movie Class
class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(30), unique=True, nullable=False)
    year = db.Column(db.Integer, nullable=False)
    description = db.Column(db.String(80), nullable=False)
    rating = db.Column(db.Float, nullable=False)
    ranking = db.Column(db.Integer, nullable=False)
    review = db.Column(db.String(30), nullable=False)
    img_url = db.Column(db.String(80), nullable=False)

    def __repr__(self) -> str:
        return '<Movie {self.title}>'


# Flask Server Routing
@app.route("/", methods=["GET", "POST"])
def home():
    all_movie = db.session.query(Movie).all()
    print(all_movie)
    return render_template("index.html", movies=all_movie)

@app.route("/edit", methods=["GET", "POST"])
def edit():
    form = MovieForm()
    id = request.args.get("id")
    movie_update = Movie.query.get(id)

    if form.validate_on_submit():
        movie_update.rating = float(form.rating.data)
        movie_update.review = form.review.data
        db.session.commit()
        return redirect(url_for('home'))
        
    return render_template("edit.html", id=id, form=form)

@app.route("/add",  methods=["GET", "POST"])
def add():
    form = GetMovieForm()
    if form.validate_on_submit():
        parameter = {
            "api_key": MOVIE_API_KEY,
            "query": form.title.data
        }
        response = requests.get(themoviedb_endpoint, params=parameter)
        response.raise_for_status()
        data = response.json()["results"]

        movies = []

        for movie in data:
            new_movie = {
                "id": movie['id'],
                "title": movie['title'],
                "release_date": movie['release_date']
            }
            movies.append(new_movie)
        return render_template("select.html", movies=movies)
    return render_template("add.html", form=form)

@app.route("/delete")
def delete():
    id = request.args.get("id")
    movie_delete = Movie.query.get(id)
    db.session.delete(movie_delete)
    db.session.commit()
    return redirect(url_for("home"))

@app.route("/select")
def select():
    id = request.args.get("id")
    parameter = {
        "api_key": MOVIE_API_KEY,
        "movie_id": id
    }    
    response = requests.get(movieDetail_endpoint + id, params=parameter)
    response.raise_for_status()
    print(response.url)
    data = response.json()
    image = "https://image.tmdb.org/t/p/original".format(data["poster_path"])
    year = data["release_date"].split("-")[0]
    movie = Movie(title=data["title"],img_url=image, year=year, description=data["overview"])
    db.session.add(movie)
    db.session.commit()
    return redirect(url_for("edit"))


if __name__ == '__main__':
    app.run(debug=True)
