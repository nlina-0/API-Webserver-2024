from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey, String
from marshmallow import fields
from init import db, ma
# from typing import List

# Is this a many to many table?

class SessionSet(db.Model):
    __tablename__="session_sets"
    id: Mapped[int] = mapped_column(primary_key=True)
    
    # Turn into foreign key
    exercise_name: Mapped[str] = mapped_column(String(200))
    exercise_set: Mapped[int]
    weight: Mapped[int]
    reps: Mapped[int]

    # foreign key: session
    session_id: Mapped[int] = mapped_column(ForeignKey("sessions.session_id"), nullable=False)
    session: Mapped["Session"] = relationship(back_populates="session_sets")

    # how to add nullable=False
    # foreign key: user_id 
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"), nullable=False))
    user: Mapped["User"] = relationship(back_populates="session_sets")

    #foreign key: exercises
    # exercise_id: Mapped[int] = mapped_column(ForeignKey("exercises.exercise_id"))
    # exercise: Mapped["Exercise"] = relationship(back_populates="session_sets")


class SessionSetSchema(ma.Schema):
    # Marshmallow validator
    exercise_name = fields.String(required=True)
    exercise_set = fields.Integer(required=True)
    weight = fields.Integer(required=True)
    reps = fields.Integer(required=True)

    # session = fields.Nested("SessionSchema", only=["session_id", "user", "date"])
    session = fields.Nested("SessionSchema", only=["session_id", "date"])
    user = fields.Nested("UserSchema", only=["id", "name"])
    # exercise = fields.Nested("ExerciseSchema", only=["exercise", "exercise_id"])
    class Meta:
        fields = ("id", "exercise_name", "exercise_set", "weight", "reps", "session")