"""views"""
from typing import Annotated

import fastapi
from fastapi import Body
from fastapi import Path

import logic

app = fastapi.FastAPI()


@app.get("/get_games_list/{user_id}")
def get_games_list(user_id: int):
    """return list of games in order of addition"""
    return logic.get_games_list(user_id)

@app.get("/get_books_list/{user_id}")
def get_books_list(user_id: int):
    """return list of books in order of addition"""
    return logic.get_books_list(user_id)

@app.get("/get_movies_list/{user_id}")
def get_movies_list(user_id: int):
    """return list of movies in order of addition"""
    return logic.get_movies_list(user_id)


@app.get("/pop_game/{user_id}")
def pop_game(
    user_id: Annotated[int, Path(title='...', ge=0)]
) -> dict:
    """return next game to play from the list"""
    return logic.pop_game(user_id)

@app.get("/pop_book/{user_id}")
def pop_book(
    user_id: Annotated[int, Path(title='...', ge=0)]
) -> dict:
    """return next book to read from the list"""
    return logic.pop_book(user_id)

@app.get("/pop_movie/{user_id}")
def pop_movie(
    user_id: Annotated[int, Path(title='...', ge=0)]
) -> dict:
    """return next movie to watch from the list"""
    return logic.pop_movie(user_id)


@app.post("/add_game/{user_id}")
def add_game(
    user_id: Annotated[int, Path()],
    title: Annotated[str, Body()],
    link: Annotated[str | None, Body()],
    priority: Annotated[int | None, Body(ge=1, le=3)],
    status: Annotated[str | None, Body()]
) -> None:
    """add new game to the list, for now in the end of the list"""
    logic.add_game(user_id, title, link, priority, status)

@app.post("/add_book/{user_id}")
def add_book(
    user_id: Annotated[int, Path()],
    title: Annotated[str, Body()],
    author: Annotated[str | None, Body()],
    link: Annotated[str | None, Body()],
    priority: Annotated[int | None, Body(ge=1, le=3)],
    status: Annotated[str | None, Body()]
) -> None:
    """add new book to the list, for now in the end of the list"""
    logic.add_book(user_id, title, author, link, priority, status)

@app.post("/add_movie/{user_id}")
def add_movie(
    user_id: Annotated[int, Path()],
    title: Annotated[str, Body()],
    link: Annotated[str | None, Body()],
    priority: Annotated[int | None, Body(ge=1, le=3)],
    status: Annotated[str | None, Body()]
) -> None:
    """add new movie to the list, for now in the end of the list"""
    logic.add_movie(user_id, title, link, priority, status)


@app.delete("delete_game/{game_id}")
def delete_game(game_id: Annotated[int, Path()]):
    """deleting game by id from db"""
    logic.delete_game(game_id)

@app.delete("delete_book/{book_id}")
def delete_book(book_id: Annotated[int, Path()]):
    """deleting book by id from db"""
    logic.delete_book(book_id)

@app.delete("delete_movie/{movie_id}")
def delete_movie(movie_id: Annotated[int, Path()]):
    """deleting movie by id from db"""
    logic.delete_movie(movie_id)


@app.post("/check_for_permition/book")
def check_for_book_permition(
    user_id: Annotated[int, Body()],
    obj_id: Annotated[int, Body()]
):
    """checks whether the given user has access to edit the book"""
    return logic.check_for_book_permition(user_id, obj_id)

@app.post("/check_for_permition/game")
def check_for_game_permition(
    user_id: Annotated[int, Body()],
    obj_id: Annotated[int, Body()]
):
    """checks whether the given user has access to edit the game"""
    return logic.check_for_game_permition(user_id, obj_id)

@app.post("/check_for_permition/movie")
def check_for_movie_permition(
    user_id: Annotated[int, Body()],
    obj_id: Annotated[int, Body()]
):
    """checks whether the given user has access to edit the movie"""
    return logic.check_for_movie_permition(user_id, obj_id)

@app.patch("/change_game_priority/{game_id}")
def change_game_priority(
    game_id: Annotated[int, Path()],
    new_priority: Annotated[int, Body()]
):
    return logic.change_game_priority(game_id, new_priority)

@app.patch("/change_book_priority/{book_id}")
def change_book_priority(
    book_id: Annotated[int, Path()],
    new_priority: Annotated[int, Body()]
):
    return logic.change_book_priority(book_id, new_priority)

@app.patch("/change_movie_priority/{movie_id}")
def change_movie_priority(
    movie_id: Annotated[int, Path()],
    new_priority: Annotated[int, Body()]
):
    return logic.change_movie_priority(movie_id, new_priority)


@app.patch("change_book_status/{book_id}")
def change_book_status(
    book_id: Annotated[int, Path()],
    new_status: Annotated[str, Body()]
):
    return logic.change_book_status(book_id, new_status)

@app.patch("change_game_status/{game_id}")
def change_game_status(
    game_id: Annotated[int, Path()],
    new_status: Annotated[str, Body()]
):
    return logic.change_game_status(game_id, new_status)

@app.patch("change_movie_status/{movie_id}")
def change_movie_status(
    movie_id: Annotated[int, Path()],
    new_status: Annotated[str, Body()]
):
    return logic.change_movie_status(movie_id, new_status)
