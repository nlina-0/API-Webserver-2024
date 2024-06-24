from datetime import date
from flask import Blueprint, request
from flask_jwt_extended import jwt_required, get_jwt_identity
from models.session import Session, SessionSchema
from models.user import User
# from models.session_set import SessionSet, SessionSetSchema
from init import db


sessions_bp = Blueprint("sessions", __name__, url_prefix="/sessions")

# Get all sessions (R)
@sessions_bp.route("")
@jwt_required()
def get_sessions():
    stmt = db.select(Session)
    sessions = db.session.scalars(stmt).all()
    session_schema = SessionSchema(many=True, exclude=["session_sets"])
    return session_schema.dump(sessions)


# Get session by ID (R)
@sessions_bp.route("/<int:session_id>")
def get_session_by_id(session_id):
    session = db.get_or_404(Session, session_id)
    return SessionSchema().dump(session)


# Create session (C)
@sessions_bp.route("/", methods=["POST"])
@jwt_required()
def create_session():
    user_id = get_jwt_identity()
    user = db.get_or_404(User, user_id)

    session = Session(
        date=date.today(),
        user=user
    )

    db.session.add(session)
    db.session.commit()
    return SessionSchema().dump(session), 201


# Delete session (D)
@sessions_bp.route("/<int:id>", methods=["DELETE"])
@jwt_required()
def delete_session(id):
    session = db.get_or_404(Session, id)
    db.session.delete(session)
    db.session.commit()
    return {}
