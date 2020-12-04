from flask import Blueprint
from models import User
from extensions import db

user = Blueprint("user", __name__)

@user.route("/")
def home():
    return "User home page"

@user.route("/add/<id>/<name>")
def add(id,name):
    user = User(id=id,name=name)
    db.session.add(user)
    db.session.commit()
    return "user added"

@user.route("/test")
def test():
    a = 2