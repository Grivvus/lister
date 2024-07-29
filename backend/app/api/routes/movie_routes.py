from typing import Annotated

from fastapi import APIRouter, Path, Body

from app.models import Movie
from app.logic import movies_logic

router = APIRouter()


@router.get("/get_all_movies")
async def get_all_movies():
    """
    returns all movies in order of addition to db
    """
    return await movies_logic.get_all_movies()


@router.get("/get_movies_in_rate_order")
async def get_movies_in_rate_order():
    """
    returns all movies in decreasing order of rate
    """
    return await movies_logic.get_movies_in_rate_order()


@router.get("/pop_movie")
async def pop_movie():
    """
    returns movie with highest rate that not read yet
    """
    return await movies_logic.pop_movie()


@router.post("/add_movie")
async def add_movie(movie_data: Annotated[Movie, Body()]):
    """
    add new movie to db
    """
    return await movies_logic.add_movie(movie_data)


@router.delete("/remove_movie/{movie_name}")
async def remove_movie(movie_name: Annotated[str, Path()]):
    """
    removing movie by name
    """
    return await movies_logic.remove_movie(movie_name)


@router.patch("change_movie_name/{movie_name}")
async def change_movie_name(
    movie_name: Annotated[str, Path()],
    new_movie_name: Annotated[str, Body()]
):
    """
    change movie name or throws HTTPException
    if there's no such movie
    """
    return await movies_logic.change_movie_name(movie_name, new_movie_name)


@router.patch("change_movie_status/{movie_name}")
async def change_movie_status(
    movie_name: Annotated[str, Path()],
    new_status: Annotated[str, Body()]
):
    """
    change movie status or throws HTTPException
    if there's no such movie or status is incorrect
    """
    return await movies_logic.change_movie_status(movie_name, new_status)


@router.patch("change_movie_rate/{movie_name}")
async def change_movie_rate(
    movie_name: Annotated[str, Path()],
    new_rate: Annotated[int, Body()]
):
    """
    change movie rate or throws HTTPException
    if there's no such movie or rate is incorrect
    """
    return await movies_logic.change_movie_rate(movie_name, new_rate)


@router.patch("change_movie_review/{movie_name}")
async def change_movie_review(
    movie_name: Annotated[str, Path()],
    new_review: Annotated[str, Body()]
):
    """
    change movie review or throws HTTPException
    if there's no movie
    """
    return await movies_logic.change_movie_review(movie_name, new_review)


@router.patch("change_movie_genre/{movie_name}")
async def change_movie_genre(
    movie_name: Annotated[str, Path()],
    new_movie_genre: Annotated[str, Body()]
):
    """
    change movie genre or throws HTTPException
    if there's no such movie
    """
    return await movies_logic.change_movie_genre(movie_name, new_movie_genre)


@router.patch("change_movie_director/{movie_name}")
async def change_movie_director(
    movie_name: Annotated[str, Path()],
    new_director: Annotated[str, Body()]
):
    """
    change movie director or throws HTTPException
    if there's no such movie
    """
    return await movies_logic.change_movie_director(movie_name, new_director)
