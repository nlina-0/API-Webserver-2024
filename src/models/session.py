from datetime import date
from init import db, ma
from sqlalchemy.orm import Mapped, mapped_column

class Session(db.Model):
    __tablename__="sessions"
    id: Mapped[int] = mapped_column(primary_key=True)
    date: Mapped[date]
