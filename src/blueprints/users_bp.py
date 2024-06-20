from flask import Blueprint, request
from models.user import User, UserSchema
from init import db, bcrypt

users_bp = Blueprint("users", __name__, url_prefix="/users")

# Get all users (R); Admin only
@users_bp.route("")
def get_users():
    stmt = db.select(User)
    users = db.session.scalars(stmt).all()
    return UserSchema(many=True).dump(users)

# Register (P); User - Not completed
@users_bp.route("/register", methods=["POST"])
def create_user():
    # Load is used to run the incoming request through the user schema
    params = UserSchema(only=["name", "email"]).load(request.json)
    return params

# Login (P); All
@users_bp.route("/login", methods=["POST"])
def login():
    email = request.json["email"]
    password = request.json["password"]
    stmt = db.select(User).where(User.email == email)
    # scalar returns single tuple
    user = db.session.scalar(stmt)
    if user and bcrypt.check_password_hash(user.password, password):
        pass
    else:
        return {"error": "Invalid email or password"}, 401
    
    print(vars(user))
    return "ok"