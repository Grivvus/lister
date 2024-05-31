from beanie import init_beanie
from motor.motor_asyncio import AsyncIOMotorClient

from app.models import Book, Game, Movie
from app.core.settings import settings


async def init_db():
    client = AsyncIOMotorClient(
        f"mongodb://{settings.MONGO_INITDB_ROOT_USERNAME}:"
        + f"{settings.MONGO_INITDB_ROOT_PASSWORD}@0.0.0.0:27017"
    )

    await init_beanie(
        database=client.db_name, document_models=[
            Book, Game, Movie
        ]
    )
