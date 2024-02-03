"""views for interaction with db"""
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
):
    """return next game to play from the list"""
    return logic.pop_game(user_id)

@app.get("/pop_book/{user_id}")
def pop_book(
    user_id: Annotated[int, Path(title='...', ge=0)]
):
    """return next book to read from the list"""
    return logic.pop_book(user_id)

@app.get("/pop_movie/{user_id}")
def pop_movie(
    user_id: Annotated[int, Path(title='...', ge=0)]
):
    """return next movie to watch from the list"""
    return logic.pop_movie(user_id)

# планы на будущее
@app.get()
def get_random_game():
    raise NotImplementedError()

@app.get()
def get_random_book():
    raise NotImplementedError()

@app.get()
def get_random_movie():
    raise NotImplementedError()

@app.post("/add_game/{user_id}")
def add_game(
    user_id: Annotated[int, Path()],
    title: Annotated[str, Body()],
    link: Annotated[str | None, Body()],
    priority: Annotated[int | None, Body(ge=1, le=3)]
) -> None:
    """add new game to the list, for now in the end of the list"""
    logic.add_game(user_id, title, link, priority)

@app.post("/add_book/{user_id}")
def add_book(
    user_id: Annotated[int, Path()],
    title: Annotated[str, Body()],
    author: Annotated[str | None, Body()],
    link: Annotated[str | None, Body()],
    priority: Annotated[int | None, Body(ge=1, le=3)]
) -> None:
    """add new book to the list, for now in the end of the list"""
    logic.add_book(user_id, title, author, link, priority)

@app.post("/add_movie/{user_id}")
def add_movie(
    user_id: Annotated[int, Path()],
    title: Annotated[str, Body()],
    link: Annotated[str | None, Body()],
    priority: Annotated[int | None, Body(ge=1, le=3)]
) -> None:
    """add new movie to the list, for now in the end of the list"""
    logic.add_movie(user_id, title, link, priority)


@app.delete()
def delete_game():
    raise NotImplementedError()

@app.delete()
def delete_book():
    raise NotImplementedError()

@app.delete()
def delete_movie():
    raise NotImplementedError()


@app.patch()
def change_game_priority():
    raise NotImplementedError()

@app.patch()
def change_book_priority():
    raise NotImplementedError()

@app.patch()
def change_movie_priority():
    raise NotImplementedError()
