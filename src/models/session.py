from datetime import date
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey
from init import db, ma
from typing import List
from marshmallow import fields

class Session(db.Model):
    __tablename__="sessions"
    session_id: Mapped[int] = mapped_column(primary_key=True)
    date: Mapped[date]

    # Foreign key
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"), nullable=False)
    user: Mapped["User"] = relationship(back_populates="sessions")

    session_sets: Mapped[List["SessionSet"]] = relationship(back_populates="session", cascade="all, delete")

class SessionSchema(ma.Schema):
    user = fields.Nested("UserSchema", only=["id", "name"])
    session_sets = fields.List(fields.Nested("SessionSetSchema", only=[ "id", "exercise_name", "exercise_set", "weight", "reps"]))
    class Meta:
        fields = ("session_id", "date", "user", "session_sets")
