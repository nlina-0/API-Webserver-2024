from flask import Blueprint, request, abort
from models.exercise import Exercise, ExerciseSchema
from init import db
from auth import admin_only

exercises_bp = Blueprint("exercises", __name__, url_prefix="/exercises")

# Only admin can create, update and delete

# Get all exercises (R); All
@exercises_bp.route("")
def all_exercises():
    stmt = db.select(Exercise)
    exercises = db.session.scalars(stmt).all()
    return ExerciseSchema(many=True).dump(exercises)


# Get one exercise (R); All
@exercises_bp.route("/<int:id>")
def one_exercise(id):
    exercise = db.get_or_404(Exercise, id)
    return ExerciseSchema().dump(exercise)


# Create exercise (C); Admin only
@exercises_bp.route("", methods=["POST"])
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
def update_exercise(id):
    stmt = db.select(Exercise).filter_by(exercise_id=id)
    exercises = db.session.scalar(stmt)
    if not exercises:
        abort(404)

    exercise_update = ExerciseSchema(only=["exercise", "description"], unknown="exclude").load(request.json)

    exercises.exercise = exercise_update.get("exercise", exercises.exercise)
    exercises.description = exercise_update.get("description", exercises.description)

    db.session.commit()
    return ExerciseSchema().dump(exercises), 201



# Delete exercise (D); Admin only



# Get list of user exercises (R)