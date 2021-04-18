from flask import Flask, render_template
import requests
app = Flask(__name__)

genderize_endpoint = "https://api.genderize.io/?"
agifiy_endpoint = "https://api.agify.io/?"


@app.route('/')
def home():
    return render_template("index.html")

@app.route('/guess/<name>')
def guess(name):
    
    genderize_response = requests.get(genderize_endpoint+"name={}".format(name))
    print(genderize_response.text)
    genderize_response.raise_for_status()
    
    agifiy_response = requests.get(agifiy_endpoint+"name={}".format(name))
    agifiy_response.raise_for_status()
    
    gender_data = genderize_response.json()
    agifiy_data = agifiy_response.json()

    return render_template("guess.html", name=name, gender=gender_data["gender"], age=agifiy_data["age"])

@app.route('/blog')
def get_blog():
    fake_blog_endpoint = "https://api.npoint.io/5abcca6f4e39b4955965"
    response = requests.get(fake_blog_endpoint)
    all_posts = response.json()
    return render_template("blog.html", posts=all_posts)

if __name__ == "__main__":
    app.run(debug=True)


