from init import db
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String

class User(db.Model):
    __tablename__="users"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(100))
    email: Mapped[str] = mapped_column(String(200), unique=True)
    # password: Mapped[str] = mapped_column(String(200))
