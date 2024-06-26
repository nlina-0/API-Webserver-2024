from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, Text
from marshmallow import fields
from init import db, ma
from typing import List

# Use composite key to combine ID and exercise

class Exercise(db.Model):
    __tablename__="exercises"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(100))
    description: Mapped[str] = mapped_column(Text())

    # exercises: Mapped[List["SessionExercise"]] = relationship(back_populates="exercise", cascade='all, delete-orphan')

class ExerciseSchema(ma.Schema):
    class Meta:
        fields = ("id", "name", "description")