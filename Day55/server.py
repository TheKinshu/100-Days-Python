from flask import Flask, render_template
import random

app = Flask(__name__)

answer = random.randint(0,9)

game_bg = "https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif"

high = "https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif"

low = "https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif"

correct = "https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif"

@app.route("/")
def home():
    html = "Guess a number between 0 and 9"
    print(answer)
    return render_template("index.html", html=html, image=game_bg)


@app.route("/<number>")
def guess(number):
    num = int(number)
    if num > answer:
        return render_template("index.html", html="Too high, try again!",  image=high)
    elif num < answer:
        return render_template("index.html", html="Too low, try again!",  image=low)
    else:
        return render_template("index.html", html="You found me!",  image=correct)

if __name__ == "__main__":
    app.run(debug=True)
