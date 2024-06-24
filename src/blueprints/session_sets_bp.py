from flask import Blueprint, request
from flask_jwt_extended import jwt_required
from models.session import Session
from models.session_set import SessionSet, SessionSetSchema
from init import db

session_sets_bp = Blueprint("session_sets", __name__, url_prefix="/session-sets")

# Get session set by ID (R)
@session_sets_bp.route("/<int:id>")
def get_session_sets_by_id(id):
    session_set = db.get_or_404(SessionSet, id)
    session_set_schema = SessionSetSchema(exclude=["session"])
    return session_set_schema.dump(session_set)


# Create session set (C)
@session_sets_bp.route("/", methods=["POST"])
@jwt_required()
def create_session_set():
    # Get the latest Session_ID
    session = db.session.query(Session).order_by(Session.session_id.desc()).first()
    latest_session_id = session.session_id

    session_set_info = SessionSetSchema(only=["exercise_name", "exercise_set", "weight", "reps", "session"]).load(request.json)
    session_set = SessionSet(
        exercise_name=session_set_info["exercise_name"],
        exercise_set=session_set_info["exercise_set"],
        weight=session_set_info["weight"],
        reps=session_set_info["reps"],
        session_id=latest_session_id
    )
    db.session.add(session_set)
    db.session.commit()
    return SessionSetSchema().dump(session_set)


# Update session set (U)


# Delete session set (D)


