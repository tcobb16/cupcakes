"""Flask app for Cupcakes"""

from flask import Flask, jsonify, request, render_template
from models import db, connect_db, Cupcake


app = Flask(__name__)

app.config["SECRET_KEY"] = "ohsosecret"
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql:///cupcakes"


connect_db(app)


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/api/cupcakes")
def get_cupcakes():
    all_cupcakes = Cupcake.query.all()
    serialized = {
        "cupcakes": [c.to_dict for c in all_cupcakes]
    }

    return jsonify(serialized)


@app.route("/api/cupcakes/<int:cupcake_id>")
def single_cupcake(cupcake_id):
    cupcake = Cupcake.query.get_or_404(cupcake_id)
    serialized = {
        "cupcake": cupcake.to_dict
    }

    return jsonify(serialized)


@app.route("/api/cupcakes", methods=["POST"])
def create_cupcake():
    data = request.json 
    cupcake = Cupcake(
        **data
    )

    db.session.add(cupcake)
    db.session.commit()

    serialized = {
        "cupcake": cupcake.to_dict
    }

    return jsonify(serialized), 201



@app.route("/api/cupcakes/<int:cupcake_id>", methods=["PATCH"])
def update_cupcake(cupcake_id):
    cupcake = Cupcake.query.get_or_404(cupcake_id)
    data = request.json 

    cupcake.flavor = data["flavor"]
    cupcake.size = data["size"]
    cupcake.rating = data["rating"]
    if "image" in data:
        cupcake.image = data["image"]

    db.session.commit()

    serialized = {
        "cupcake": cupcake.to_dict
    }

    return jsonify(serialized), 201



@app.route("/api/cupcakes/<int:cupcake_id>", methods=["DELETE"])
def delete_cupcake(cupcake_id):
    cupcake = Cupcake.query.get_or_404(cupcake_id)

    db.session.delete(cupcake)

    db.session.commit()

    serialized = {
        "message": "Deleted"
    }

    return jsonify(serialized), 201
