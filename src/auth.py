from flask_jwt_extended import jwt_required, get_jwt_identity
from init import db
from models.user import User

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


# Ensure the JWT user is the owner of the session