from fastapi import APIRouter

from app.api.routes import book_routes, game_routes, movie_routes
from app.core.db import ping

api_router = APIRouter()
api_router.include_router(
    book_routes.router, prefix="/books", tags=["book"]
)
api_router.include_router(
    game_routes.router, prefix="/games", tags=["game"]
)
api_router.include_router(
    movie_routes.router, prefix="/movies", tags=["movie"]
)


@api_router.get("/ping")
async def database_ping():
    return ping()
