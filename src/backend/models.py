"""there's all sqlalchemy models for my bot"""
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import TIMESTAMP
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.sql import func


class Base(DeclarativeBase):
    pass


class Book(Base):
    """model represents book with additional info about it"""

    __tablename__ = "book"

    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(Integer())
    title: Mapped[str] = mapped_column(String(50))
    author: Mapped[str] = mapped_column(String(), nullable=True)
    link: Mapped[str] = mapped_column(String(), nullable=True)
    # pririty is number between 1 and 3, 1 - most wanted, 3 - less wanted
    priority: Mapped[int] = mapped_column(Integer(), default=3)
    # there's 3 statuses: o - opened, c - closed, p - in progress
    status: Mapped[str] = mapped_column(String(1), default="o")
    added_at: Mapped[TIMESTAMP] = mapped_column(
        TIMESTAMP(timezone=True),
        server_default=func.now(),
    )
    taken_at: Mapped[TIMESTAMP] = mapped_column(
        TIMESTAMP(timezone=True), nullable=True
    )
    closed_at: Mapped[TIMESTAMP] = mapped_column(
        TIMESTAMP(timezone=True), nullable=True
    )
    # optional add time when persen start to interact with book, game, etc...
    # started_reading = ...

    # come up with idea of sorting books by importance for person
    # тут надо на ux подумать, как эту сортировку будет делать пользователь

    def __repr__(self) -> str:
        return f"Book(id={self.id}, title={self.title}, \
            link={self.link})"


class Game(Base):
    """model represents game with additional info about it"""

    __tablename__ = "game"

    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(Integer())
    title: Mapped[str] = mapped_column(String(50))
    link: Mapped[str] = mapped_column(String())
    # pririty is number between 1 and 3, 1 - most wanted, 3 - less wanted
    priority: Mapped[int] = mapped_column(Integer(), default=3)
    # there's 3 statuses: o - opened, c - closed, p - in progress
    status: Mapped[str] = mapped_column(String(1), default="o")
    added_at: Mapped[TIMESTAMP] = mapped_column(
        TIMESTAMP(timezone=True),
        server_default=func.now(),
    )
    taken_at: Mapped[TIMESTAMP] = mapped_column(
        TIMESTAMP(timezone=True), nullable=True
    )
    closed_at: Mapped[TIMESTAMP] = mapped_column(
        TIMESTAMP(timezone=True), nullable=True
    )

    def __repr__(self) -> str:
        return f"Game(id={self.id}, title={self.title}, \
            link={self.link})"


class Movie(Base):
    """model represents movie(series) with additional info"""

    __tablename__ = "movie"

    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(Integer())
    title: Mapped[str] = mapped_column(String(50))
    link: Mapped[str] = mapped_column(String())
    # pririty is number between 1 and 3, 1 - most wanted, 3 - less wanted
    priority: Mapped[int] = mapped_column(Integer())
    # there's 3 statuses: o - opened, c - closed, p - in progress
    status: Mapped[str] = mapped_column(String(1), default="o")
    added_at: Mapped[TIMESTAMP] = mapped_column(
        TIMESTAMP(timezone=True),
        server_default=func.now(),
    )
    taken_at: Mapped[TIMESTAMP] = mapped_column(
        TIMESTAMP(timezone=True), nullable=True
    )
    closed_at: Mapped[TIMESTAMP] = mapped_column(
        TIMESTAMP(timezone=True), nullable=True
    )

    def __repr__(self) -> str:
        return f"Movie(id={self.id}, title={self.title}, \
            link={self.link})"
