from typing import Annotated

from fastapi import APIRouter, Body, Path

from app.models import Game
from app.logic import games_logic

router = APIRouter()


@router.get("/get_all_games")
async def get_all_games():
    """
    returns all games in order of addition to db
    """
    return await games_logic.get_all_games()


@router.get("/get_games_in_rate_order")
async def get_games_in_rate_order():
    """
    returns all games in decreasing order of rate
    """
    return await games_logic.get_games_in_rate_order()


@router.get("/pop_game")
async def pop_game():
    """
    returns game with highest rate that not read yet
    """
    return await games_logic.pop_game()


@router.post("/add_game")
async def add_game(game_data: Annotated[Game, Body()]):
    """
    add new game to db or throws HTTPException
    if some parameters are incorrect
    """
    return await games_logic.add_game(game_data)


@router.delete("/remove_game/{game_name}")
async def remove_game(game_name: Annotated[str, Path()]):
    """
    removing game by name or throws HTTPException
    if there's no such game
    """
    return await games_logic.remove_game(game_name)


@router.patch("/change_game_name/{game_name}")
async def change_game_name(
    game_name: Annotated[str, Path()],
    new_game_name: Annotated[str, Body()]
):
    """
    change game name or throws HTTPException
    if there's no such game
    """
    return await games_logic.change_game_name(game_name, new_game_name)


@router.patch("/change_game_status/{game_name}")
async def change_game_status(
    game_name: Annotated[str, Path()],
    new_status: Annotated[str, Body()]
):
    """
    change game status or throws HTTPException
    if there's no such game or new status is incorrect
    """
    return await games_logic.change_game_status(game_name, new_status)


@router.patch("/change_game_rate/{game_name}")
async def change_game_rate(
    game_name: Annotated[str, Path()],
    new_rate: Annotated[int, Body()]
):
    """
    change game rate or throws HTTPException
    if there's no game or new_rate is incorrect
    """
    return await change_game_rate(game_name, new_rate)


@router.patch("/change_game_review/{game_name}")
async def change_game_review(
    game_name: Annotated[str, Path()],
    new_review: Annotated[str, Body()]
):
    """
    change game review or throws HTTPException
    if there's no such game
    """
    return await change_game_review(game_name, new_review)


@router.patch("/change_game_genre/{game_name}")
async def change_game_genre(
    game_name: Annotated[str, Path()],
    new_game_genre: Annotated[str, Body()]
):
    """
    change game genre or throws HTTPException
    if there's no such game
    """
    return await games_logic.change_game_genre(game_name, new_game_genre)
