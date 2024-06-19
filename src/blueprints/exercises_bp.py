from flask import Blueprint
from models.exercise import Exercise, ExerciseSchema
from init import db

exercises_bp = Blueprint("exercises", __name__, url_prefix="/exercises")

# Get all exercises (R); All
@exercises_bp.route("")
def get_exercises():
    stmt = db.select(Exercise)
    exercises = db.session.scalars(stmt).all()
    return ExerciseSchema(many=True).dump(exercises)
