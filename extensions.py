from flask_sqlalchemy import SQLAlchemy
from flask_wtf import CsrfProtect

db = SQLAlchemy()
csrf = CsrfProtect()