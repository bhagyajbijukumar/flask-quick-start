from flask import Blueprint, render_template, request, redirect, session, render_template_string, url_for
from models import User
from extensions import db
from helpers.userhelpers import create_user, login as login_, current_user
import sqlalchemy
from forms import SignUpForm

from helpers.userhelpers import login_required, current_user

user = Blueprint("user", __name__)

@user.route("/")
@login_required
def home():
    user = current_user()
    return render_template("index.html", user=user)


@user.route("/signup/", methods=["GET","POST"])
def signup():
    if request.method == 'GET':
        form = SignUpForm()
        return render_template("signup.html", form=form)
    elif request.method == 'POST':
        username = request.form.get('username')
        email = request.form.get('email')
        password = request.form.get('password')
        try:
            token = create_user(username=username, email=email, password=password,verified=True)
        except sqlalchemy.exc.IntegrityError:
            return "User already exists"

        session["user"] = token
        return redirect(url_for("user.home"))


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
            return redirect(url_for("user.home"))
        else:
            return "invalid params"

@user.route("/logout")
def logout():
    session.pop("user", None)
    return redirect(url_for("user.home"))

