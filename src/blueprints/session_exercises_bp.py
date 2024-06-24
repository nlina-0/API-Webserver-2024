from flask import Blueprint
from models.session_exercise import SessionExercise, SessionExerciseSchema
from init import db

session_exercises_bp = Blueprint("session_exercise", __name__, url_prefix="/session-exercise")

@session_exercises_bp.route("")
def get_session_exercises():
    stmt = db.select(SessionExercise)
    session_exercises = db.session.scalars(stmt).all()
    return SessionExerciseSchema(many=True).dump(session_exercises)

# Get session exercise based on user_id