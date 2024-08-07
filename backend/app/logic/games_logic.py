import pymongo
from pymongo.results import DeleteResult

from app.models import Game
from app.logic.validation import (
    validate_rate,
    validate_status,
    validate_status_and_rate,
    validate_status_and_review,
)


async def get_all_games() -> list[Game]:
    """
    returns all games as list
    """
    return await Game.find().to_list()


async def get_games_in_rate_order() -> list[Game]:
    """
    returns all games that have rate in descending order
    """
    games_list = await Game.find(
        Game.rate is not None
    ).sort(
        (Game.rate, pymongo.DESCENDING)
    ).to_list()

    return games_list


async def pop_game() -> Game | None:
    """
    returns game that not played yet from top of to_list
    and change game status to 'in progress'
    """
    game = await Game.find_one(Game.status == "not started")
    if game is not None:
        game.status("in progress")
        await game.save()

    return game


async def add_game(game_data: Game) -> Game:
    """
    add new game to db
    or throws HTTPException if some data incorrect
    """
    validate_status(game_data.status)
    validate_rate(game_data.rate)
    validate_status_and_rate(game_data.status, game_data.rate)
    validate_status_and_review(game_data.status, game_data.review)
    new_game = Game(
        name=game_data.name,
        status=game_data.status,
        rate=game_data.rate,
        review=game_data.review,
        add_time=game_data.add_time,
        change_time=game_data.change_time,
        genre=game_data.genre
    )

    return await new_game.insert()


async def get_game_by_name(game_name: str) -> Game | None:
    """
    search for game by it's name
    """
    game = await Game.find_one(Game.name == game_name)
    return game


async def remove_game(game_name: str) -> None:
    """
    removes game from db
    """
    game = await get_game_by_name(game_name)
    if game is not None:
        await game.delete()
    return None


async def change_game_name(game_name: str, new_game_name: str) -> Game | None:
    """
    change game name
    """
    game = await get_game_by_name(game_name)
    if game is not None:
        game.name = new_game_name
        return await game.save()
    return None


async def change_game_status(game_name: str, new_status: str) -> Game | None:
    """
    change game status or throws HTTPException
    if status is incorrect
    """
    validate_status(new_status)
    game = await get_game_by_name(game_name)
    if game is not None:
        game.status = new_status
        return await game.save()
    return None


async def change_game_rate(game_name: str, new_rate: int) -> Game | None:
    """
    change game status or throws HTTPException
    if new rate is incorrect
    """
    validate_rate(new_rate)
    game = await get_game_by_name(game_name)
    if game is not None:
        validate_status_and_rate(game.status, new_rate)
        game.rate = new_rate
        return await game.save()
    return None


async def change_game_review(game_name: str, new_reivew: str) -> Game | None:
    """
    change game review or throws HTTPException
    """
    game = await get_game_by_name(game_name)
    if game is not None:
        validate_status_and_review(game.status, new_reivew)
        game.review = new_reivew
        return await game.save()
    return None


async def change_game_genre(game_name: str, new_genre: str) -> Game | None:
    """
    change game genre
    """
    game = await get_game_by_name(game_name)
    if game is not None:
        game.genre = new_genre
        return await game.save()
    return None
