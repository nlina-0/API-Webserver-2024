from flask import Blueprint, request
from flask_jwt_extended import jwt_required, get_jwt_identity
from models.session import Session
from models.session_set import SessionSet, SessionSetSchema
from models.user import User
from init import db
from auth import authorize_owner

session_sets_bp = Blueprint("session_sets", __name__, url_prefix="/session-sets")

# # Get session_set (R): User must be the owner of session_set
@session_sets_bp.route("/<int:id>")
@jwt_required()
def get_session_sets_by_id(id):
    session_set = db.get_or_404(SessionSet, id)
    authorize_owner(session_set)
    return SessionSetSchema().dump(session_set)  
    

# Create session set (C)
@session_sets_bp.route("/", methods=["POST"])
@jwt_required()
def create_session_set():
    user_id = get_jwt_identity()
    user = db.get_or_404(User, user_id)
    user_info = user.id
    
    # Get the latest Session_ID, session_sets can only be created after the user has created a new session, or if the session selected belongs to them
    session = db.session.query(Session).order_by(Session.session_id.desc()).first()
    session_user = session.user_id 
    if session_user != user_info:
        return {"error": "You must be the session owner. Create a new session to become session owner."}, 403
    
    latest_session_id = session.session_id

    session_set_info = SessionSetSchema(only=["exercise_name", "exercise_set", "weight", "reps", "session"], unknown="exclude").load(request.json)
    session_set = SessionSet(
        exercise_name=session_set_info["exercise_name"],
        exercise_set=session_set_info["exercise_set"],
        weight=session_set_info["weight"],
        reps=session_set_info["reps"],
        session_id=latest_session_id,
        user=user
    )
    db.session.add(session_set)
    db.session.commit()
    return SessionSetSchema().dump(session_set), 201


# Update session set (U): User must be the owner of session_set
@session_sets_bp.route("/<int:id>", methods=["PUT", "PATCH"])
@jwt_required()
def update_session_set(id):
    session_set = db.get_or_404(SessionSet, id)
    authorize_owner(session_set)

    session_set_info = SessionSetSchema(only=["id", "exercise_name", "exercise_set", "weight", "reps"], unknown="exclude").load(request.json)

    session_set.id = session_set_info.get("id", session_set.id) # Has to be an existing session though
    session_set.exercise_name = session_set_info.get("exercise_name", session_set.exercise_name)
    session_set.exercise_set = session_set_info.get("exercise_set", session_set.exercise_set)
    session_set.weight = session_set_info.get("weight", session_set.weight)
    session_set.reps = session_set_info.get("reps", session_set.reps)
    
    db.session.commit()
    return SessionSetSchema().dump(session_set), 201


# Delete session set (D): User must be the owner of session_set (check to see what happens when deletes somebody elses session_set)
@session_sets_bp.route("/<int:id>", methods=["DELETE"])
@jwt_required()
def delete_session(id):
    session_set = db.get_or_404(SessionSet, id)
    authorize_owner(session_set)
    db.session.delete(session_set)
    db.session.commit()
    return {}

