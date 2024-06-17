from flask import Blueprint
from models.user import User
from init import app, db

db_commands = Blueprint('spam', __name__)

@db_commands.cli.command("create")
def db_create():
    db.drop_all()
    db.create_all()
    print("Created tables")