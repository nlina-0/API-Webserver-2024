from init import db, ma
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String, Text
from marshmallow import fields

class Exercise(db.Model):
    __tablename__="exercises"
    id: Mapped[int] = mapped_column(primary_key=True)
    exercise: Mapped[str] = mapped_column(String(100))
    description: Mapped[str] = mapped_column(Text())

class ExerciseSchema(ma.Schema):
    class Meta:
        fields = ("id", "exercise", "description")