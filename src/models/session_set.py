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


    # Link relationship between Session_Exercises to Exercises
    # foreign key: exercise (Id and exercise)
    # exercise_id: Mapped[int] = mapped_column(ForeignKey("exercises.id", ondelete="CASCADE"))
    # exercise: Mapped["Exercise"] = relationship(back_populates="session_exercises")

    # foreign key: session
    session_id: Mapped[int] = mapped_column(ForeignKey("sessions.id"))
    session: Mapped["Session"] = relationship(back_populates="session_sets")


class SessionSetSchema(ma.Schema):
    session = fields.Nested("SessionSchema", only=["id", "user", "date"])
    class Meta:
        # Still need to add session id
        fields = ("exercise_name", "session", "exercise_set", "weight", "reps")