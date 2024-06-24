from flask import Blueprint
from models.exercise import Exercise, ExerciseSchema
from init import db

exercises_bp = Blueprint("exercises", __name__, url_prefix="/exercises")

# Only admin can edit

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

# Edit exercise (U); Admin only

# Delete exercise (D); Admin only
