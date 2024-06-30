from typing import List, Optional
from marshmallow import fields
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, Boolean
from init import db, ma
from marshmallow.validate import Length

class User(db.Model):
    __tablename__="users"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[Optional[str]] = mapped_column(String(100))
    email: Mapped[str] = mapped_column(String(200), unique=True)
    password: Mapped[str] = mapped_column(String(200))
    is_admin: Mapped[bool] = mapped_column(Boolean(), server_default="false")

    # Associations
    sessions: Mapped[List["Session"]] = relationship(back_populates="user", cascade="all, delete")
    session_sets: Mapped[List["SessionSet"]] = relationship(back_populates="user", cascade="all, delete")


class UserSchema(ma.Schema):
    # Marshmallow validator
    email = fields.Email(required=True)
    password = fields.String(validate=Length(min=8, error='Password must be at least 8 characters long'), required=True)

    sessions = fields.List(fields.Nested("SessionSchema", exclude=["user"]))

    class Meta:
        fields = ("id", "name", "email", "password", "is_admin", "sessions")