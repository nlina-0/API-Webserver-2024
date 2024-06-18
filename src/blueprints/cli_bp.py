from flask import Blueprint
from models.user import User
from init import db

db_commands = Blueprint('spam', __name__)

@db_commands.cli.command("create")
def db_create():
    db.drop_all()
    db.create_all()
    print("Created tables")

@db_commands.cli.command("seed")
def seed_db():
    users = [
        User(
            name="John Doe",
            email="doe@mail.com"
        ),
        User(
            name="Sam Jane",
            email="jane@mail.com"
        )
    ]

    db.session.add_all(users)
    db.session.commit()

    print("Users added")