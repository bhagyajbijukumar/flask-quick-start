from flask import Blueprint, render_template
from models import User
from extensions import db

user = Blueprint("user", __name__)

@user.route("/")
def home():
    return render_template("index.html")


@user.route("/signup/")
def signup():
    return render_template("signup.html")

