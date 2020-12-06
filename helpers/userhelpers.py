from extensions import db
from models import User
import bcrypt, string, random

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
    hashed = user.password
    if bcrypt.checkpw(password.encode('utf-8'), hashed):
        return user
    else:
        return False