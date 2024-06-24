from flask import Blueprint
from models.session_set import SessionSet, SessionSetSchema
from init import db

session_sets_bp = Blueprint("session_sets", __name__, url_prefix="/session-set")

@session_sets_bp.route("")
def get_session_sets():
    stmt = db.select(SessionSet)
    session_sets = db.session.scalars(stmt).all()
    return SessionSetSchema(many=True).dump(session_sets)

# Get session exercise based on user_id