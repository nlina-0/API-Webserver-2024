from init import db, ma
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String
from marshmallow import fields

class User(db.Model):
    __tablename__="users"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(100))
    email: Mapped[str] = mapped_column(String(200), unique=True)

# Creates user schema with marshmallow; provides serialization needed for converting data into JSON
class UserSchema(ma.Schema):
    # Marshmallow validator, ensures that what is entered is an email
    email = fields.Email(required=True)
    class Meta:
        fields = ("id", "name", "email")