from beanie import Document, Indexed
from pydantic import BaseModel
import pymongo


class Game(Document):
    name: str
    description: str
    rate: int
    review: str
