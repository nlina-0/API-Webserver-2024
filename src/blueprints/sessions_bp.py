from datetime import date
from flask import Blueprint
from flask_jwt_extended import jwt_required, get_jwt_identity
from models.session import Session, SessionSchema
from models.user import User
from init import db
from auth import admin_only, authorize_owner



sessions_bp = Blueprint("sessions", __name__, url_prefix="/sessions")

# Get all sessions (R): Admin only
@sessions_bp.route("")
@jwt_required()
@admin_only
def get_sessions():
    stmt = db.select(Session)
    sessions = db.session.scalars(stmt).all()
    session_schema = SessionSchema(many=True, exclude=["session_sets"])
    return session_schema.dump(sessions)


# Get all user sessions (R): User must be owner of sessions
@sessions_bp.route("/user")
@jwt_required()
def get_user_sessions():
    user_id = get_jwt_identity()
    stmt = db.select(Session).where(Session.user_id == user_id)
    sessions = db.session.scalars(stmt).all()
    session_schema = SessionSchema(many=True, exclude=["session_sets"])
    return session_schema.dump(sessions)



# Get session by ID (R): User must be owner of sessions otherwise an error occurs
@sessions_bp.route("/<int:session_id>")
@jwt_required()
def get_session_by_id(session_id):
    session = db.get_or_404(Session, session_id)
    authorize_owner(session)
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


# Delete session (D): User must be owner of sessions otherwise an error occurs
@sessions_bp.route("/<int:id>", methods=["DELETE"])
@jwt_required()
def delete_session(id):
    session = db.get_or_404(Session, id)
    authorize_owner(session)
    db.session.delete(session)
    db.session.commit()
    return {}


# Update session (U):
# If admin creates session, admin should be able to update session user? Admin can only update to existing user