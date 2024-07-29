from typing import Annotated
import datetime

from beanie import Document, Indexed


class GenericItem(Document):
    """
    model that represents generic item in  db
    """
    name: Annotated[str, Indexed()]
    genre: str
    status: str  # надо бы сделать типо enum [not_sarted, in_progress, finished] smth like that
    rate: int | None
    review: str | None
    add_time: datetime.datetime
    change_time: datetime.datetime | None


class Book(GenericItem):
    """
    model that represents book entity
    """
    author: str

    class Settings:
        name = "books"


class Game(GenericItem):
    """
    model that represents game entity
    """

    class Settings:
        name = "games"


class Movie(GenericItem):
    """
    model that represents movie entity
    """
    director: str | None

    class Settings:
        name = "movies"
