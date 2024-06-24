from flask import Blueprint, request
from models.session import Session
from models.session_set import SessionSet, SessionSetSchema
from init import db

session_sets_bp = Blueprint("session_sets", __name__, url_prefix="/session-sets")

# # Get all session sets (R): NOT NEEDED
# @session_sets_bp.route("")
# def get_session_sets():
#     stmt = db.select(SessionSet)
#     session_sets = db.session.scalars(stmt).all()
#     return SessionSetSchema(many=True).dump(session_sets)

# Get session set by ID (R)
@session_sets_bp.route("/<int:id>")
def get_session_sets_by_id(id):
    session_set = db.get_or_404(SessionSet, id)
    session_set_schema = SessionSetSchema(exclude=["session"])
    return session_set_schema.dump(session_set)

# Create session set (C)
@session_sets_bp.route("/", methods=["POST"])
def create_session_set():
    session_set_info = SessionSetSchema(only=["exercise_name", "exercise_set", "weight", "reps", "session"]).load(request.json)
    session_set = SessionSet(
        exercise_name=session_set_info["exercise_name"],
        exercise_set=session_set_info["exercise_set"],
        weight=session_set_info["weight"],
        reps=session_set_info["reps"],
        # session_id= (need to create a session_id)
    )
    db.session.add(session_set)
    db.session.commit()
    return SessionSetSchema().dump(session_set)

# request args?


# # Get session set by exercise name (R): NOT NEEDED
# @session_sets_bp.route("<string:exercise>")
# def get_session_set_by_exercise(exercise):
#     upper_exercise = exercise.capitalize()
#     stmt = db.select(SessionSet).where(SessionSet.exercise_name == upper_exercise)
#     session_set = db.session.scalars(stmt).all()
#     return SessionSetSchema(many=True).dump(session_set)
