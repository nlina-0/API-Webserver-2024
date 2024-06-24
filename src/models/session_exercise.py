from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey, String
from marshmallow import fields
from init import db, ma
from typing import List

# Is this a many to many table?

class SessionExercise(db.Model):
    __tablename__="session_exercises"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(100))

    # Link relationship between Session_Exercises to Exercises
    # foreign key: exercise (Id and exercise)
    # exercise_id: Mapped[int] = mapped_column(ForeignKey("exercises.id", ondelete="CASCADE"))
    # exercise: Mapped["Exercise"] = relationship(back_populates="session_exercises")

    # foreign key: session
    session_id: Mapped[int] = mapped_column(ForeignKey("sessions.id"))
    session: Mapped["Session"] = relationship(back_populates="session_exercises")

    # relationship to exercise_set
    exercise_sets: Mapped[List["ExerciseSet"]] = relationship(back_populates="session_exercise")

class SessionExerciseSchema(ma.Schema):
    session = fields.Nested("SessionSchema", only=["id", "user", "date"])
    exercise_sets = fields.List(fields.Nested("ExerciseSetSchema", exclude=["session_exercise"]))
    class Meta:
        # Still need to add session id
        fields = ("name", "session", "exercise_sets")