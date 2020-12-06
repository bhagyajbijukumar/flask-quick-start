from extensions import db
from models import User
import bcrypt

def create_user(username, email, password, verified=False, is_staff=False):
    pwd = password.encode('utf-8')
    from main import create_app
    app = create_app(config_file="config.cfg")
    salt = bcrypt.gensalt()
    hashed=bcrypt.hashpw(pwd, salt)
    
    with app.app_context():
        user = User(username=username, email=email, password=hashed, verified=verified, is_staff=False)
        db.session.add(user)
        db.session.commit()