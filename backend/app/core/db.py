from beanie import init_beanie
from motor.motor_asyncio import AsyncIOMotorClient

from app.models import Game
from app.core.settings import settings


async def init_db():
    client = AsyncIOMotorClient(
        f"mongodb://{settings.MONGO_INITDB_ROOT_USERNAME}:"
        + f"{settings.MONGO_INITDB_ROOT_PASSWORD}@0.0.0.0:27017"
    )

    await init_beanie(database=client.db_name)


async def test_insert():
    game1 = Game(
        name="The Witcher 3",
        descriptiot="the game about adventures Geralt of Rivia",
        rate=10,
        review="best action RPG ever"
    )
    await game1.insert()
