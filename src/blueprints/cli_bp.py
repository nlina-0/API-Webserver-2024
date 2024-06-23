from datetime import date
from flask import Blueprint
from models.user import User
from models.exercise import Exercise
from models.session import Session
from models.exercise_set import ExerciseSet
from models.session_exercise import SessionExercise
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
            name="Squat",
            description="Lower body exercise."
        ),
        Exercise(
            name="Deadlift",
            description="Full body exercise."
        ),
        Exercise(
            name="Pull up",
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
            date=date.today(),
            user=users[1]
        ),
        Session(
            date=date.today(),
            user=users[2]
        )
    ]

    db.session.add_all(sessions)
    db.session.commit()

    session_exercise = [
        # has to be created by user...how?
        SessionExercise(
            name="Squat",
            # have a nested value to show the description
            session=sessions[0],
        ),
        SessionExercise(
            name="Deadlift",
            # have a nested value to show the description
            session=sessions[2]
        )
    ]

    db.session.add_all(session_exercise)
    db.session.commit()

    exercise_set = [
        ExerciseSet(
            exercise_set="1",
            weight="20",
            reps="12"
        )
    ]

    db.session.add_all(exercise_set)
    db.session.commit()

    print("Users, Exercises, Sessions, Exercise sets and Session exercises added")