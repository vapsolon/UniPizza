from flask import Flask
from flask_bcrypt import Bcrypt
app = Flask(__name__)
bcrypt = Bcrypt(app)

from flask_sqlalchemy import SQLAlchemy
import os

if os.environ.get("HEROKU"):
    app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DATABASE_URL")
else:
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///unipizza.db" 
    app.config["SQLALCHEMY_ECHO"] = True

db = SQLAlchemy(app)

import application.views

from application.product import models
from application.product import views

from application.ingredient import models
from application.ingredient import views

from application.cart import views

from application.order import models
from application.order import views

from application.auth import models
from application.auth import views

from application.auth.models import User
app.config["SECRET_KEY"] = b'>\xb3\xfb\x0b\xa12\xc8\x99\xf1\x91\x85a\x08x\xc7\xcfRc\xe5\xe4\x0ch[\xb7\xe8\x1am\x17U\xead\xbf'

from flask_login import LoginManager
login_manager = LoginManager()
login_manager.init_app(app)

login_manager.login_view = "auth_login"
login_manager.login_message = "Please log in to use this functionality."

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

try: 
    db.create_all()
except:
    pass