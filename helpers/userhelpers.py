from flask import session, request, url_for, redirect
from extensions import db
from models import User
import bcrypt, string, random
from functools import wraps

def generate_id(size:int=60):
    chars=string.ascii_uppercase + string.digits + string.ascii_lowercase
    return ''.join(random.choice(chars) for _ in range(size))

def create_user(username, email, password, verified=False, is_staff=False):
    pwd = password.encode('utf-8')
    from main import create_app
    app = create_app(config_file="config.cfg")
    salt = bcrypt.gensalt()
    hashed=bcrypt.hashpw(pwd, salt)
    while True:
        token = generate_id()
        exists = User.query.filter_by(token=token).first()
        if not exists: break
    print(token)
    with app.app_context():
        user = User(username=username, email=email, password=hashed, verified=verified, is_staff=False, token=token)
        db.session.add(user)
        db.session.commit()
        return token

def login(email:str, password:str):
    user = User.query.filter_by(email=email).first()
    if user:
        hashed = user.password
    else:
        return False
    if bcrypt.checkpw(password.encode('utf-8'), hashed):
        return user.token
    else:
        return False

def validate_token(token):
    user = User.query.filter_by(token=token).first()
    if user:
        return user
    else:
        return None



def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        user = None
        if "user" in session.keys():
            token = session["user"]
            user = validate_token(token)
        else:
            return redirect(url_for('user.login', next=request.url))
        if not user:
            return redirect(url_for('user.login', next=request.url))
        return f(*args, **kwargs)
    return decorated_function

def current_user():
    token = session["user"]
    user = validate_token(token)
    print(user)
    return user