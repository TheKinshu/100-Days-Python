from flask import Flask, render_template, redirect
from flask.helpers import url_for
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms import validators
from wtforms.fields.core import SelectField
from wtforms.validators import DataRequired
import csv

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap(app)

cRating = ["☕", "☕☕", "☕☕☕", "☕☕☕☕", "☕☕☕☕☕"]
wRaiting = ["✘","💪","💪💪","💪💪💪","💪💪💪💪","💪💪💪💪💪"]
sRating = ["✘","🔌","🔌🔌","🔌🔌🔌","🔌🔌🔌🔌","🔌🔌🔌🔌🔌"]

class CafeForm(FlaskForm):
    cafe = StringField('Cafe name', validators=[DataRequired()])
    location =StringField('Cafe Location on Google Maps (URL)', validators=[DataRequired(), validators.URL()])
    openTime = StringField('Opening Time e.g. 8AM', validators=[DataRequired()])
    closeTime = StringField('Closing time e.g. 5:30PM', validators=[DataRequired()])
    coffeeRate = SelectField('Coffee Rating', choices=cRating)
    wifiRate = SelectField('Wifi Strength Rating', choices=wRaiting)
    socketNum = SelectField('Power Socket Availability', choices=sRating)
    submit = SubmitField('Submit')

# all Flask routes below
@app.route("/")
def home():
    return render_template("index.html")


@app.route('/add', methods=["GET", "POST"])
def add_cafe():
    form = CafeForm()
    if form.validate_on_submit():
        cafeInfo = [form.cafe.data, form.location.data, form.openTime.data, form.closeTime.data, form.coffeeRate.data, form.wifiRate.data, form.socketNum.data]
        cafe = ",".join(cafeInfo)
        with open('./Day62/cafe-data.csv', 'a', encoding="utf8") as file:
            file.write("\n{}".format(cafe))
        return redirect(url_for('cafes'))
    return render_template('add.html', form=form)


@app.route('/cafes')
def cafes():
    with open('./Day62/cafe-data.csv', newline='', encoding="utf8") as csv_file:
        csv_data = csv.reader(csv_file, delimiter=',')
        list_of_rows = []
        for row in csv_data:
            list_of_rows.append(row)
    return render_template('cafes.html', cafes=list_of_rows)


if __name__ == '__main__':
    app.run(debug=True)
