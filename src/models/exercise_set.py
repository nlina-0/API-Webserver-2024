from sqlalchemy.orm import Mapped, mapped_column
from init import db, ma

class ExerciseSet(db.Model):
    __tablename__="exercise_sets"
    id: Mapped[int] = mapped_column(primary_key=True)
    # session_exercise_id (foreign key)
    # Should I add exercise name? 
    # Is exercise set needed? Can that just be defined by the ID
    exercise_set: Mapped[int]
    weight: Mapped[int]
    reps: Mapped[int]
    # foreign key: session exercise

class ExerciseSetSchema(ma.Schema):
    class Meta:
        fields = ("id", "exercise_set", "weight", "reps")