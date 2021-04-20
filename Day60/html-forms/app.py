from flask import Flask, render_template, request
import smtplib

app = Flask(__name__)
my_email = "kelvc.app@gmail.com"
password = "jhljkmlnwhsybpkx"

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/contact', methods=["GET", "POST"])
def about():
    if request.method == "POST":

        name = request.form["name"]
        email = request.form["email"]
        phone = request.form["phone"]
        msg = request.form["message"]

        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(my_email, password)
            connection.sendmail(
                from_addr=my_email,
                to_addrs=my_email,
                msg="Subject:New Message\n\n\
                    Name: {} \n\
                    Email: {} \n\
                    Phone Number: {} \n\
                    Message: {} \n\
                    ".format(name, email, phone, msg)
            )
        return "<h1>Successful Sent Message</h1>"

    return render_template("contact.html")


@app.route('/login', methods=["GET", "POST"])
def receive_data():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        return "<h1>Name: {} Password: {}</h1>".format(username, password)
    return "Nothing here"



if __name__ == "__name__":
    app.run(debug=True)