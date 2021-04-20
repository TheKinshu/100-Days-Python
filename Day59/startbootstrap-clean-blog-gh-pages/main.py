# Importing different modules from the internet
from flask import Flask, render_template
from post import Post
import requests

# Creating an flask application call app
app = Flask(__name__)

# URL for NPoint API
url = "https://api.npoint.io/5abcca6f4e39b4955965"

# Grabbing the contents that the API provides
response = requests.get(url)
# Checks for error code and stops the program if found
response.raise_for_status()

# Convert contents into a JSON file 
data = response.json()

blogs = [Post(blog['id'], blog['title'], blog['subtitle'], blog['body']) for blog in data]

# Flask server linking to different address
# -------------------------------------------
@app.route('/')
def home():
    return render_template("index.html")

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/post')
def post():
    return render_template("post.html", posts=data)

@app.route('/post/<id>')
def get_post(id):
    return render_template("blog", blog=blogs[id])
    
@app.route('/contact')
def contact():
    return render_template("contact.html")

# Check for the current program name -
# if program name is not main don't run
if __name__ == "__main__":
    app.run(debug=True)