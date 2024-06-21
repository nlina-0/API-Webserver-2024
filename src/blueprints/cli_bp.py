from datetime import date
from flask import Blueprint
from models.user import User
from models.exercise import Exercise
from models.session import Session
from init import db, bcrypt

db_commands = Blueprint('db', __name__)

@db_commands.cli.command("create")
def db_create():
    db.drop_all()
    db.create_all()
    print("Created tables")

    users = [
        User(
            # name="John Doe",
            email="doe@mail.com",
            password=bcrypt.generate_password_hash("123456").decode("utf8"),
            is_admin=True
        ),
        User(
            name="Sam Jane",
            email="jane@mail.com",
            password=bcrypt.generate_password_hash("523456").decode("utf8")
        )
    ]

    db.session.add_all(users)
    db.session.commit()

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

    sessions = [
        Session(
            date=date.today()
        ),
        Session(
            date=date.today()
        )
    ]

    db.session.add_all(sessions)
    db.session.commit()

    print("Users added")
    print("Exercises added")
    print("Sessions added")