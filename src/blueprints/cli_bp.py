from datetime import date
from flask import Blueprint
from models.user import User
from models.exercise import Exercise
from models.session import Session
from models.session_set import SessionSet
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
        ),
        User(
            name="Finn Star",
            email="star@mail.com",
            password=bcrypt.generate_password_hash("password").decode("utf8")
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
        ),
        Exercise(
            exercise="Pull up",
            description="Upper body exercise."
        )
    ]

    db.session.add_all(exercises)
    db.session.commit()

    sessions = [
        Session(
            date=date.today(),
            # User instance
            user=users[1]
        ),
        Session(
            date="2024-06-22",
            user=users[2]
        )
    ]

    db.session.add_all(sessions)
    db.session.commit()

    session_set = [
        # has to be created by user...how?
        SessionSet(
            exercise_name="Squat",
            # have a nested value to show the description
            session=sessions[0],
            exercise_set="1",
            weight="40",
            reps="10",
            user=users[1]
        ),
        SessionSet(
            exercise_name="Squat",
            session=sessions[0],
            exercise_set="2",
            weight="60",
            reps="8",
            user=users[1]
        ),
        SessionSet(
            exercise_name="Squat",
            session=sessions[1],
            exercise_set="1",
            weight="40",
            reps="10",
            user=users[2]
        ),
        SessionSet(
            exercise_name="Deadlift",
            session=sessions[0],
            exercise_set="1",
            weight="40",
            reps="10",
            user=users[1]
        )
    ]

    db.session.add_all(session_set)
    db.session.commit()

    print("Users added")
    print("Exercises added")
    print("Sessions added")
    print("Session sets added")