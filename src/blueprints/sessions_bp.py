from flask import Blueprint, request
from flask_jwt_extended import jwt_required
from models.session import Session, SessionSchema
from models.exercise_set import ExerciseSet, ExerciseSetSchema
from init import db


sessions_bp = Blueprint("sessions", __name__, url_prefix="/sessions")

# Get all session (R)
@sessions_bp.route("")
# If logged in as user, user can can only access own sessions
@jwt_required()
def get_sessions():
    stmt = db.select(Session)
    sessions = db.session.scalars(stmt).all()
    return SessionSchema(many=True).dump(sessions)

# Get all exercise set (R)
@sessions_bp.route("/exercise_set")
# If logged in as user, user can can only access own sessions
@jwt_required()
def get_exercise_sets():
    stmt = db.select(ExerciseSet)
    exercise_set = db.session.scalars(stmt).all()
    return ExerciseSetSchema(many=True).dump(exercise_set)

# Create session exercise sets (C)
@sessions_bp.route("/", methods=["POST"])
# Only users and admins can use this function
# @jwt_required
def create_exercise_set():
    # How would I link this exercise set model (set info for each exercise performed) to the session model (id, date)?
    session_info = ExerciseSetSchema(only=["exercise_set", "weight", "reps"], unknown="exclude").load(request.json)
    session = ExerciseSet(
        exercise_set=session_info["exercise_set"],
        weight=session_info["weight"],
        reps=session_info["reps"]
    )
    db.session.add(session)
    db.session.commit()
    return ExerciseSetSchema().dump(session), 201

# Update an existing exercise set (U)
@sessions_bp.route("/<int:id>", methods=["PUT", "PATCH"])
# @jwt_required
def update_exercise_set(id):
    exercise_set = db.get_or_404(ExerciseSet, id)
    session_info = ExerciseSetSchema(only=["exercise_set", "weight", "reps"], unknown="exclude").load(request.json)
    # Should the user be the one to create the set number? Or should that be computer generated by ID?
    exercise_set.weight = session_info.get("weight", exercise_set.weight)
    exercise_set.reps = session_info.get("reps", exercise_set.reps)
    db.session.commit()
    return ExerciseSetSchema().dump(exercise_set)

# Delete exercise_set (D)
@sessions_bp.route("/<int:id>", methods=["DELETE"])
# @jwt_required
def delete_exercise_set(id):
    exercise_set = db.get_or_404(ExerciseSet, id)
    db.session.delete(exercise_set)
    db.session.commit()
    return {}
