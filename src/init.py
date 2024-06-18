from os import environ
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase
from flask_marshmallow import Marshmallow

# What does this do? Part of SQLAlchemy
class Base(DeclarativeBase):
    pass

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = environ.get("DB_URI")

db = SQLAlchemy(model_class=Base)
# Why do i need this?
db.init_app(app)
ma = Marshmallow(app)