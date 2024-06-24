from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey
from init import db, ma
from marshmallow import fields

class ExerciseSet(db.Model):
    __tablename__="exercise_sets"
    id: Mapped[int] = mapped_column(primary_key=True)
    # session_exercise_id (foreign key)
    # Should I add exercise name? 
    # Is exercise set needed? Can that just be defined by the ID; Exercise set should be unique
    exercise_set: Mapped[int]
    weight: Mapped[int]
    reps: Mapped[int]

    # foreign key: session exercise
    session_exercise_id: Mapped[int] = mapped_column(ForeignKey("session_exercises.id"))
    session_exercise: Mapped["SessionExercise"] = relationship(back_populates="exercise_sets")

class ExerciseSetSchema(ma.Schema):
    session_exercise = fields.Nested("SessionExerciseSchema", only=["name", "session"])
    
    class Meta:
        fields = ("exercise_set", "weight", "reps", "session_exercise")