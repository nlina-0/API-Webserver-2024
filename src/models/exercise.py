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

class ExerciseSchema(ma.Schema):
    exercise = fields.String(required=True)
    description = fields.String(required=True)

    class Meta:
        fields = ("exercise_id", "exercise", "description")