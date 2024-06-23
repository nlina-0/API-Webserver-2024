from flask import Blueprint
from models.exercise import Exercise, ExerciseSchema
from init import db

exercises_bp = Blueprint("exercises", __name__, url_prefix="/exercises")

# Exercises should only be modified by Admin

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

