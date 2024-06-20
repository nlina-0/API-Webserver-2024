from os import environ
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase
from flask_marshmallow import Marshmallow
from flask_bcrypt import Bcrypt

# Part of SQLAlchemy, stores all the meta data and column mappings of models
class Base(DeclarativeBase):
    pass

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = environ.get("DB_URI")

db = SQLAlchemy(model_class=Base)
db.init_app(app)
ma = Marshmallow(app)
bcrypt = Bcrypt(app)