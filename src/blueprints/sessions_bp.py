from flask import Blueprint
from models.session import Session, SessionSchema
from init import db
from flask_jwt_extended import jwt_required

sessions_bp = Blueprint("sessions", __name__, url_prefix="/sessions")

@sessions_bp.route("")
@jwt_required()
def get_sessions():
    stmt = db.select(Session)
    sessions = db.session.scalars(stmt).all()
    return SessionSchema(many=True).dump(sessions)