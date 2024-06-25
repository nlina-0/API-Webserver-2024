from datetime import timedelta
from flask import Blueprint, request
from flask_jwt_extended import create_access_token, jwt_required
from models.user import User, UserSchema
from init import db, bcrypt
from auth import admin_only


users_bp = Blueprint("users", __name__, url_prefix="/users")

# Get all users (R); Admin only
@users_bp.route("")
# Also checks for existing user - using the subject in the token
@jwt_required()
@admin_only
def get_users():
    stmt = db.select(User)
    users = db.session.scalars(stmt).all()
    user_schema = UserSchema(many=True, exclude=["sessions", "password"])
    return user_schema.dump(users)
    

# Register (P); User can create account
@users_bp.route("/register", methods=["POST"])
def create_user():
    params = UserSchema(only=["name", "email", "password"], unknown="exclude").load(request.json)

    user = User(
        email=params["email"],
        name=params["name"],
        password=params["password"],
        is_admin=False
    )

    db.session.add(user)
    db.session.commit()

    user_schema = UserSchema(exclude=["sessions"])
    return user_schema.dump(user), 201


# Login (P); All
@users_bp.route("/login", methods=["POST"])
def login():
    # unknown=exclude will exclude any invalid fields
    params = UserSchema(only=["email", "password"]).load(request.json, unknown="exclude")
    stmt = db.select(User).where(User.email == params["email"])
    # scalar returns single tuple
    user = db.session.scalar(stmt)
    
    if user and bcrypt.check_password_hash(user.password, params["password"]):
        # Creates JWT token
        # additional_claims={"email": user.email, "name": user.name},
        token = create_access_token(identity=user.id, expires_delta=timedelta(hours=2))
        return {"token": token}
    else:
        return {"error": "Invalid email or password"}, 401