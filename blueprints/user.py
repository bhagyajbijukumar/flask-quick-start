from flask import Blueprint, render_template, request
from models import User
from extensions import db
from helpers.userhelpers import create_user

user = Blueprint("user", __name__)

@user.route("/")
def home():
    return render_template("index.html")


@user.route("/signup/", methods=["GET","POST"])
def signup():
    if request.method == 'GET':
        return render_template("signup.html")
    elif request.method == 'POST':
        username = request.form.get('username')
        email = request.form.get('email')
        password = request.form.get('password')
        create_user(username=username, email=email, password=password,verified=True)
        return "User created"

