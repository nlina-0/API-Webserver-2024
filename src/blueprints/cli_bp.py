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
            # name="Admin One",
            email="admin@mail.com",
            password=bcrypt.generate_password_hash("12345678").decode("utf8"),
            is_admin=True
        ),
        User(
            name="Blue Two",
            email="blue@mail.com",
            password=bcrypt.generate_password_hash("12345678").decode("utf8")
        ),
        User(
            name="Green Three",
            email="green@mail.com",
            password=bcrypt.generate_password_hash("12345678").decode("utf8")
        )
    ]

    db.session.add_all(users)
    db.session.commit()

    exercises = [
        Exercise(
            exercise="Squat",
            description="A compound, full-body exercise that primarily targets the muscles of the thighs, hips, and buttocks, as well as strengthening the bones, ligaments, and insertion of the tendons throughout the lower body."
        ),
        Exercise(
            exercise="Deadlift",
            description="A strength training exercise in which a person lifts a loaded barbell or bar off the ground from a stabilized, bent-over position."
        ),
        Exercise(
            exercise="Pull up",
            description="A strength training exercise that targets the upper body, specifically the muscles of the back, shoulders, and arms."
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
            user=users[1],
            # exercise=exercises[0]
        ),
        SessionSet(
            exercise_name="Squat",
            session=sessions[0],
            exercise_set="2",
            weight="60",
            reps="8",
            user=users[1],
            # exercise=exercises[0]
        ),
        SessionSet(
            exercise_name="Squat",
            session=sessions[1],
            exercise_set="1",
            weight="40",
            reps="10",
            user=users[2],
            # exercise=exercises[0]
        ),
        SessionSet(
            exercise_name="Deadlift",
            session=sessions[0],
            exercise_set="1",
            weight="40",
            reps="10",
            user=users[1],
            # exercise=exercises[1]
        )
    ]

    db.session.add_all(session_set)
    db.session.commit()

    print("Users added")
    print("Exercises added")
    print("Sessions added")
    print("Session sets added")