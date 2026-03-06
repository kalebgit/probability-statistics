from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String, Integer
from base import Base


class User(Base):
    __tablename__ = "user"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(100), nullable=False)
    email: Mapped[str] = mapped_column(String(200), nullable=False)

    def __repr__(self):
        return f"<User(id={self.id}, name={self.name}, email={self.email})"

