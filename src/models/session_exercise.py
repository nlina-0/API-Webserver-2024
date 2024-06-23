from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey, String
from init import db, ma
from marshmallow import fields

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

# Create Schema
class SessionExerciseSchema(ma.Schema):
    # exercise = fields.Nested("UserSchema", only=["name", "description"])
    class Meta:
        # Still need to add session id
        fields = ("name", )