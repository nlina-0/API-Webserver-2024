from datetime import timedelta
from flask import Blueprint, request, abort
from flask_jwt_extended import create_access_token, jwt_required
from models.user import User, UserSchema
from init import db, bcrypt
from auth import admin_only, get_jwt_identity, authorize_owner


users_bp = Blueprint("users", __name__, url_prefix="/users")

# Get all users (R); Admin only
@users_bp.route("")
@jwt_required() # Do I need this if theres a jwt_required in the decorator of admin_only?
@admin_only
def get_users():
    stmt = db.select(User)
    users = db.session.scalars(stmt).all()
    user_schema = UserSchema(many=True, exclude=["sessions", "password"])
    return user_schema.dump(users)
    

# Register (C); User can create account
@users_bp.route("/register", methods=["POST"])
def create_user():
    params = UserSchema(only=["name", "email", "password"], unknown="exclude").load(request.json)

    user = User(
        email=params["email"],
        name=params["name"],
        password=bcrypt.generate_password_hash(params["password"]).decode("utf8"),
        is_admin=False
    )

    db.session.add(user)
    db.session.commit()

    user_schema = UserSchema(exclude=["sessions"])
    return user_schema.dump(user), 201


# Login (C); All
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
    

# Update account (U): User can update acc
@users_bp.route("", methods=["PUT", "PATCH"])
@jwt_required()
def update_user_acc():
    user_id = get_jwt_identity()
    stmt = db.select(User).where(User.id == user_id)
    user = db.session.scalar(stmt)

    user_update = UserSchema(only=["email", "name", "password"], unknown="exclude").load(request.json)

    user.email = user_update.get("email", user.email)
    user.name = user_update.get("name", user.name)
    user.password = user_update.get("password", user.password)

    db.session.commit()
    return UserSchema().dump(user), 201


# Get all users (R); Admin only
@users_bp.route("/<int:id>", methods=["DELETE"])
@jwt_required()
def del_user(id):
    user_id = get_jwt_identity()
    stmt = db.select(User).where(User.id == user_id, User.is_admin)
    user = db.session.scalar(stmt)
    if user:
        stmt = db.select(User).where(User.id == id)
        user = db.session.scalar(stmt)
        if user:
            db.session.delete(user)
            db.session.commit()
            return {}
        else:
            return {"error": "User does not exist"}, 404
    else:
        return {"error": "You must be an admin to access this resource"}, 403

    