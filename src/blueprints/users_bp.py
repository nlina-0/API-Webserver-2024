from flask import Blueprint
from models.user import User, UserSchema
from init import db

users_bp = Blueprint("users", __name__)

# Get all users (R); Admin only
@users_bp.route("/users")
def get_users():
    stmt = db.select(User)
    users = db.session.scalars(stmt).all()
    return UserSchema(many=True).dump(users)