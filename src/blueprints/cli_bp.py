from flask import Blueprint
from models.user import User
from models.exercise import Exercise
from init import db

db_commands = Blueprint('spam', __name__)

@db_commands.cli.command("create")
def db_create():
    db.drop_all()
    db.create_all()
    print("Created tables")

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

    exercises = [
        Exercise(
            exercise="Squat",
            description="Lower body exercise."
        ),
        Exercise(
            exercise="Deadlift",
            description="Full body exercise."
        )
    ]

    db.session.add_all(exercises)

    db.session.commit()
    print("Users added")
    print("Exercises added")