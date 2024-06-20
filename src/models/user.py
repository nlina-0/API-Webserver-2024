from init import db, ma
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String, Boolean
from typing import List, Optional
from marshmallow import fields

class User(db.Model):
    __tablename__="users"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[Optional[str]] = mapped_column(String(100))
    email: Mapped[str] = mapped_column(String(200), unique=True)
    password: Mapped[str] = mapped_column(String(200))
    is_admin: Mapped[bool] = mapped_column(Boolean(), server_default='false')

    # Adding bidrectional association to session model
    # session: Mapped[List["Session"]] = relationship(back_populates='user')

# Creates user schema with marshmallow; provides serialization needed for converting data into JSON
class UserSchema(ma.Schema):
    # Marshmallow validator, ensures that what is entered is an email
    email = fields.Email(required=True)
    class Meta:
        fields = ("id", "name", "email")