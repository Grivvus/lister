from fastapi import APIRouter

from app.api.routes import book_routes, game_routes, movie_routes

api_router = APIRouter()
api_router.include_router(book_routes.router, prefix="/book", tags=["book"])
api_router.include_router(game_routes.router, prefix="/game", tags=["game"])
api_router.include_router(movie_routes.router, prefix="/movie", tags=["movie"])
