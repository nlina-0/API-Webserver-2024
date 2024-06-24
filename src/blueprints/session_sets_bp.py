from flask import Blueprint
from models.session import Session
from models.session_set import SessionSet, SessionSetSchema
from init import db

session_sets_bp = Blueprint("session_sets", __name__, url_prefix="/session-sets")

# Get all session sets
@session_sets_bp.route("")
def get_session_sets():
    stmt = db.select(SessionSet)
    session_sets = db.session.scalars(stmt).all()
    return SessionSetSchema(many=True).dump(session_sets)

# Get session set by ID
@session_sets_bp.route("/<int:id>")
def get_session_sets_by_id(id):
    session_set = db.get_or_404(SessionSet, id)
    session_set_schema = SessionSetSchema(exclude=["session"])
    return session_set_schema.dump(session_set)

# Get session set by exercise name
@session_sets_bp.route("<string:exercise>")
def get_session_set_by_exercise(exercise):
    upper_exercise = exercise.capitalize()
    stmt = db.select(SessionSet).where(SessionSet.exercise_name == upper_exercise)
    session_set = db.session.scalars(stmt).all()
    return SessionSetSchema(many=True).dump(session_set)
