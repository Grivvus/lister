from beanie import Document, Indexed


class GenericItem(Document):
    name: Indexed(str)
    status: str  # надо бы сделать типо enum [not_sarted, in_progress, finished] smth like that
    rate: int | None
    review: str | None
    genre: str | None


class Game(GenericItem):

    class Settings:
        name = "games"


class Book(GenericItem):
    author: str

    class Settings:
        name = "books"


class Movie(GenericItem):
    director: str | None

    class Settings:
        name = "movies"
