from flask import Blueprint, render_template
from models import User
from extensions import db

user = Blueprint("user", __name__)

@user.route("/")
def home():
    return render_template("index.html")

@user.route("/add/<id>/<name>")
def add(id,name):
    user = User(id=id,name=name)
    db.session.add(user)
    db.session.commit()
    return "user added"

