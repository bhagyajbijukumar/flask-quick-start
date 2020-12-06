from extensions import db

class User(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    username = db.Column(db.String(120), nullable=False, unique = True)
    email = db.Column(db.String(120), nullable=False, unique = True)
    password = db.Column(db.String(120), nullable=False)
    is_staff = db.Column(db.Integer, default=0, nullable = False)
    verified = db.Column(db.Boolean, default=False)
    token = db.Column(db.String(120), nullable=False, unique = True)