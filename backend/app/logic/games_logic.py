from fastapi import HTTPException
import pymongo

from app.models import Game
from app.logic.validation import (
    validat_rate,
    validate_status,
    validate_status_and_rate,
    validate_status_and_review,
)


async def get_all_games() -> list[Game]:
    """
    returns all games as list
    """
    return await Game.find().to_list()


async def get_games_in_rate_order():
    """
    returns all games that have rate in descending order
    """
    raise NotImplementedError()


async def pop_game():
    """
    returns game that not played yet from top of to_list
    and change game status to 'in progress'
    or throws HTTPException
    """
    try:
        games_list = await Game.find(Game.status == "not started").sort(
            [(Game.add_time, pymongo.DESCENDING)]
        ).to_list()
        game = games_list[0]
    except IndexError:
        raise HTTPException(
            status_code=400,
            detail="Bad request: no games to pop"
        )

    game.status("in progress")
    await game.save()

    return game


async def add_game(game_data: Game):
    """
    add new game to db
    or throws HTTPException if some data incorrect
    """
    validate_status(game_data.status)
    validat_rate(game_data.rate)
    validate_status_and_rate(game_data.status, game_data.rate)
    validate_status_and_review(game_data.status, game_data.review)
    new_game = Game(
        name=game_data.name,
        status=game_data.status,
        rate=game_data.rate,
        review=game_data.review,
        add_time=game_data.add_time,
        change_time=game_data.change_time,
        game_genre=game_data.game_genre
    )

    return await new_game.insert()


async def get_game_by_name(game_name: str) -> Game:
    """
    search for game by it's name
    """
    game = await Game.find_one(Game.name == game_name)
    if game is None:
        raise HTTPException(
            status_code=400,
            detail="Bad request: no suck game"
        )

    return game


async def remove_game(game_name: str):
    """
    removes game from db
    or throws HTTPException if there's no such game
    """
    game = await get_game_by_name(game_name)
    return await game.delete()


async def change_game_name(game_name, new_game_name):
    """
    change game name
    """
    game_to_change = await get_game_by_name(game_name)
    game_to_change.name = new_game_name

    return await game_to_change.save()


async def change_game_status(game_name, new_status):
    """
    change game status or throws HTTPException
    if status is incorrect
    """
    validate_status(new_status)
    game_to_change = await get_game_by_name(game_name)
    game_to_change.status = new_status

    return await game_to_change.save()


async def change_game_rate(game_name, new_rate):
    """
    change game status or throws HTTPException
    if new rate is incorrect
    """
    validat_rate(new_rate)
    game_to_change = await get_game_by_name(game_name)
    validate_status_and_rate(game_to_change.status, new_rate)
    game_to_change.rate = new_rate

    return await game_to_change.save()


async def change_game_review(game_name, new_reivew):
    """
    change game review or throws HTTPException
    """
    game_to_change = await get_game_by_name(game_name)
    validate_status_and_review(game_to_change.status, new_reivew)
    game_to_change.review = new_reivew

    return await game_to_change.save()


async def change_game_genre(game_name, new_genre):
    """
    change game genre
    """
    game_to_change = await get_game_by_name(game_name)
    game_to_change.game_genre = new_genre

    return await game_to_change.save()
