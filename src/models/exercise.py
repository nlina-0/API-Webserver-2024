from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, Text
from marshmallow import fields
from init import db, ma
from typing import List

# Use composite key to combine ID and exercise

class Exercise(db.Model):
    __tablename__="exercises"
    exercise_id: Mapped[int] = mapped_column(primary_key=True)
    exercise: Mapped[str] = mapped_column(String(100))
    description: Mapped[str] = mapped_column(Text())

    # exercises: Mapped[List["SessionExercise"]] = relationship(back_populates="exercise", cascade='all, delete-orphan')
    # session_sets: Mapped[List["SessionSet"]] = relationship(back_populates="exercise")

class ExerciseSchema(ma.Schema):
    class Meta:
        fields = ("exercise_id", "exercise", "description")