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

    # Foreign key is implicitly not null
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    # To establish a bidirectional relationship in one-to-many 
    user: Mapped["User"] = relationship(back_populates="sessions")

    session_sets: Mapped[List["SessionSet"]] = relationship(back_populates="session", cascade="all, delete")

class SessionSchema(ma.Schema):
    user = fields.Nested("UserSchema", only=["name"])
    session_sets = fields.List(fields.Nested("SessionSetSchema", only=["exercise_name", "exercise_set", "id"]))
    class Meta:
        fields = ("session_id", "date", "user", "session_sets")
