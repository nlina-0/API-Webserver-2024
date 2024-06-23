from marshmallow import fields
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, Boolean
from typing import List, Optional
from init import db, ma

class User(db.Model):
    __tablename__="users"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[Optional[str]] = mapped_column(String(100))
    email: Mapped[str] = mapped_column(String(200), unique=True)
    password: Mapped[str] = mapped_column(String(200))
    is_admin: Mapped[bool] = mapped_column(Boolean(), server_default="false")

    # Adding bidrectional association to session model
    sessions: Mapped[List["Session"]] = relationship(back_populates="user")

# Creates user schema with marshmallow; provides serialization needed for converting data into JSON
class UserSchema(ma.Schema):
    # Marshmallow validator, ensures that what is entered is an email
    # email = fields.Email(required=True)
    sessions = fields.List(fields.Nested("SessionSchema", exclude=["user"]))

    class Meta:
        fields = ("id", "name", "email", "password", "is_admin", "sessions")