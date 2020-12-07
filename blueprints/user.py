from flask import Blueprint, render_template, request, redirect, session, render_template_string
from models import User
from extensions import db
from helpers.userhelpers import create_user, login as login_
import sqlalchemy

from helpers.userhelpers import login_required, current_user

user = Blueprint("user", __name__)

@user.route("/")
@login_required
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
        try:
            token = create_user(username=username, email=email, password=password,verified=True)
        except sqlalchemy.exc.IntegrityError:
            return "User already exists"

        session["user"] = token
        return render_template_string("User created {{session['user']}}")


@user.route("/login", methods=["GET","POST"])
def login():
    if request.method == 'GET':
        return render_template("login.html")
    elif request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        token = login_(email, password)
        if token:
            session["user"] = token
            return redirect("/")
        else:
            return "invalid params"


        

