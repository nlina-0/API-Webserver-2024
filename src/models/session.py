from datetime import date
from init import db, ma
from sqlalchemy.orm import Mapped, mapped_column

class Session(db.Model):
    __tablename__="sessions"
    id: Mapped[int] = mapped_column(primary_key=True)
    date: Mapped[date]

    # Adding associations to this class
    # How would I force this to always have a value?
    # user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    # To establish a bidirectional relationship in one-to-many 
    # user: Mapped["User"] = relationship(back_populates="cards")
