from flask import Flask, json, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy
import random as r

app = Flask(__name__)

##Connect to Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# https://documenter.getpostman.com/view/3636961/TzJx8wdD

##Cafe TABLE Configuration
class Cafe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), unique=True, nullable=False)
    map_url = db.Column(db.String(500), nullable=False)
    img_url = db.Column(db.String(500), nullable=False)
    location = db.Column(db.String(250), nullable=False)
    seats = db.Column(db.String(250), nullable=False)
    has_toilet = db.Column(db.Boolean, nullable=False)
    has_wifi = db.Column(db.Boolean, nullable=False)
    has_sockets = db.Column(db.Boolean, nullable=False)
    can_take_calls = db.Column(db.Boolean, nullable=False)
    coffee_price = db.Column(db.String(250), nullable=True)

    def to_dict(self):
        #Method 1. 
        dictionary = {}
        # Loop through each column in the data record
        for column in self.__table__.columns:
            #Create a new dictionary entry;
            # where the key is the name of the column
            # and the value is the value of the column
            dictionary[column.name] = getattr(self, column.name)
        return dictionary
        
        #Method 2. Altenatively use Dictionary Comprehension to do the same thing.
        return {column.name: getattr(self, column.name) for column in self.__table__.columns}


@app.route("/")
def home():
    return render_template("index.html")
    

## HTTP GET - Read Record
@app.route("/random")
def random():
    all_cafes = db.session.query(Cafe).all()
    random_cafe = r.choice(all_cafes)
    # cafe_json = {
    #     "cafe" : {
    #         "id": random_cafe.id,
    #         "map_url": random_cafe.map_url,
    #         "img_url": random_cafe.img_url,
    #         "location": random_cafe.location,
    #         "seats": random_cafe.seats, 
    #         "has_toilet": random_cafe.has_toilet,
    #         "has_wifi": random_cafe.has_wifi,
    #         "has_scokets": random_cafe.has_sockets,
    #         "can_take_calls": random_cafe.can_take_calls,
    #         "coffee_price": random_cafe.coffee_price,
            
    #     }
    # }
    return  jsonify(random_cafe.to_dict())

## HTTP GET - Read All Record
@app.route("/all")
def all():
    all_cafes = db.session.query(Cafe).all()

    return jsonify(cafes=[cafe.to_dict() for cafe in all_cafes])

## HTTP GET - Find a Cafe
@app.route("/search")
def search():
    loc = request.args.get("loc")
    find_cafe = Cafe.query.filter_by(location=loc).first()
    if find_cafe == None:
        return jsonify(error={"Not Found": "Sorry, we don't have a cafe at that location."})
    return jsonify(cafe=find_cafe.to_dict())
    
## HTTP POST - Create Record
@app.route("/add", methods=["POST"])
def add():
    new_cafe = Cafe(name = request.form.get("name"),
                    map_url = request.form.get("map_url"),
                    img_url = request.form.get("img_url"),
                    location = request.form.get("location"),
                    seats = request.form.get("seats"),
                    has_toilet = bool(request.form.get("has_toilet")),
                    has_wifi = bool(request.form.get("has_wifi")),
                    has_sockets = bool(request.form.get("has_sockets")),
                    can_take_calls = bool(request.form.get("can_take_call")),
                    coffee_price = request.form.get("coffee_price")
    )
    db.session.add(new_cafe)
    db.session.commit()
    return jsonify(response = {"success": "Succesfully added the new cafe."})

## HTTP PUT/PATCH - Update Record
## Put is by sending an entire entry of data to replace the current data
## Patch is to substitute part of the data instead of the entire entry
@app.route("/update-price/<cafe_id>", methods=["PATCH"])
def update(cafe_id):
    cafe_update = Cafe.query.get(cafe_id)
    new_price = request.args.get("new_price")
    print(cafe_update)
    if cafe_update:
        cafe_update.coffee_price = new_price
        db.session.commit()
        return jsonify({"success": "Successfully updated the price."})

    return jsonify(error={"Not Found": "Sorry a cafe with that id was not found in the database."})

## HTTP DELETE - Delete Record
@app.route("/report-closed/<cafe_id>", methods=["DELETE"])
def delete(cafe_id):
    cafe = Cafe.query.get(cafe_id)
    api_key = request.args.get("api-key")
    if not api_key == "TopSecretAPIKey":
        return (jsonify(error={"Forbidden": "Sorry, that's not allowed. Make sure you have the correct api_key."}), 403)
    if not cafe:
        return (jsonify(error={"Not Found": "Sorry a cafe with that id was not found in the database"}), 404)
    db.session.delete(cafe)
    db.session.commit()
    return jsonify(response={"success": "Cafe was successfully deleted from the database."}), 200
if __name__ == '__main__':
    app.run(debug=True)
