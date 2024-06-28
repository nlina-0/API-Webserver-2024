from flask_jwt_extended import jwt_required, get_jwt_identity
from init import db
from models.user import User
from flask import abort, jsonify, make_response

# Route decorator - ensure JWT user is an admin
def admin_only(fn):
    @jwt_required()
    def inner():
        user_id = get_jwt_identity()
        stmt = db.select(User).where(User.id == user_id, User.is_admin)
        user = db.session.scalar(stmt)
        if user:
            return fn()
        else:
            return {"error": "You must be an admin to access this resource"}, 403
    
    return inner


# Ensure that the JWT user is the owner of instance
# Allow admin to bypass
def authorize_owner(obj):
    user_id = get_jwt_identity()
    
    user = db.get_or_404(User, user_id)
    user_admin = user.is_admin

    if user_id != obj.user_id and not user_admin:
        abort(make_response(jsonify(error="You must be the card owner to access this resource"), 403))


# Route decorator - ensure JWT user is an admin - test
def admin_only_in_func(fn):
    user_id = get_jwt_identity()
    stmt = db.select(User).where(User.id == user_id, User.is_admin)
    user = db.session.scalar(stmt)
    if user:
        return fn()
    else:
        return {"error": "You must be an admin to access this resource"}, 403
    