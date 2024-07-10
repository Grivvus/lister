import sys

from beanie import init_beanie

from motor.motor_asyncio import AsyncIOMotorClient, AsyncIOMotorDatabase

from app.models import Book, Game, Movie
from app.core.settings import settings


async_mongodb_client: AsyncIOMotorClient | None = None
password = settings.MONGO_INITDB_ROOT_PASSWORD
user = settings.MONGO_INITDB_ROOT_USERNAME
host = "mongodb"
port = "27017"
connection_string = f"mongodb://{user}:{password}@{host}:{port}"
db_name = settings.MONGO_DB_NAME


def get_async_mongodb_client() -> AsyncIOMotorClient:
    global async_mongodb_client
    if async_mongodb_client is None:
        async_mongodb_client = AsyncIOMotorClient(connection_string)

    return async_mongodb_client


def get_async_mongodb_database() -> AsyncIOMotorDatabase:
    global db_name
    client = get_async_mongodb_client()
    if db_name is None:
        db_name = "lister_db"
    return client[db_name]


async def start_async_mongodb() -> None:
    """
    Start beanie when process started.
    :return:
    """
    try:
        async_mongodb_database = get_async_mongodb_database()
        await init_beanie(
            database=async_mongodb_database,
            document_models=[
                Book, Game, Movie
            ],
        )
        print("started mongodb connection")
    except Exception as e:
        print(f"Failed to start mongodb. error={e}")
        sys.exit(1)

if __name__ == "__main__":
    print(connection_string)
