from flask import Blueprint, request, abort
from flask_jwt_extended import jwt_required, get_jwt_identity
from models.exercise import Exercise, ExerciseSchema
from models.user import User
from init import db
from auth import admin_only

exercises_bp = Blueprint("exercises", __name__, url_prefix="/exercises")

# Only admin can create, update and delete

# Get all exercises (R); All
@exercises_bp.route("")
def all_exercises():
    stmt = db.select(Exercise)
    exercises = db.session.scalars(stmt).all()
    return ExerciseSchema(many=True).dump(exercises), 200


# Get one exercise (R); All
@exercises_bp.route("/<int:id>")
def one_exercise(id):
    exercise = db.get_or_404(Exercise, id)
    return ExerciseSchema().dump(exercise), 200


# Create exercise (C); Admin only
@exercises_bp.route("", methods=["POST"])
@jwt_required()
@admin_only
def create_exercise():
    new_exercise = ExerciseSchema(only=["exercise", "description"], unknown="exclude").load(request.json)
    exercise = Exercise(
        exercise=new_exercise["exercise"],
        description=new_exercise["description"]
    )
    db.session.add(exercise)
    db.session.commit()
    return ExerciseSchema().dump(exercise), 201


# Update exercise (U); Admin only
@exercises_bp.route("/<int:id>", methods=["PUT", "POST"])
@jwt_required()
def update_exercise(id):
    user_id = get_jwt_identity()
    stmt = db.select(User).where(User.id == user_id, User.is_admin)
    user = db.session.scalar(stmt)
    # If user is admin
    if user:    
        stmt = db.select(Exercise).filter_by(exercise_id=id)
        exercises = db.session.scalar(stmt)
        if not exercises:
            abort(404)
        else:
            exercise_update = ExerciseSchema(only=["exercise", "description"], unknown="exclude").load(request.json, partial=True)
            exercises.exercise = exercise_update.get("exercise", exercises.exercise)
            exercises.description = exercise_update.get("description", exercises.description)
            db.session.commit()
            return ExerciseSchema().dump(exercises), 200
    else:
        return {"error": "You must be an admin to access this resource"}, 403



# Delete exercise (D); Admin only
@exercises_bp.route("/<int:id>", methods=["DELETE"])
@jwt_required()
def delete_exercise(id):
    user_id = get_jwt_identity()
    # create function for this:
    stmt = db.select(User).where(User.id == user_id, User.is_admin)
    user = db.session.scalar(stmt)
    if user:
        stmt = db.select(Exercise).filter_by(exercise_id=id)
        exercise = db.session.scalar(stmt)
        if not exercise:
            abort(404)
        else:
            db.session.delete(exercise)
            db.session.commit()
            return {}    
    else:
        return {"error": "You must be an admin to access this resource"}, 403





# # Get exercise by name. Currently not working - leave til the end.
# @exercises_bp.route("/<exercise>")
# def get_exercise_by_name(exercise):
#     exercise_upper = exercise.title()
#     # stmt = db.session.query(Exercise).filter(Exercise.exercise == exercise_upper)
#     # stmt = db.session.query(Exercise).filter(Exercise.exercise_id == exercise)
#     
# stmt = db.session.query(Exercise, SessionSet).join(SessionSet, Exercise.exercise == SessionSet.exercise_name).filter(Exercise.exercise == SessionSet.exercise_name)
#     exercise = db.session.scalar(stmt)
#     print(exercise.exercise_id)
#     return ExerciseSchema().dump(exercise)


# Can I match exercise name to exercise_name in table?
# SessionSet.exercise_name == Exercise.exercise

# stmt = db.session.query(Exercise, SessionSet).join(SessionSet, Exercise.exercise == SessionSet.exercise_name).filter(Exercise.exercise == SessionSet.exercise_name)
# 
# exercise = db.session.scalar(stmt)


