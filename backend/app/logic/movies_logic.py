from fastapi import HTTPException
import pymongo

from app.models import Movie
from app.logic.validation import (
    validate_rate,
    validate_status,
    validate_status_and_rate,
    validate_status_and_review,
)


async def get_all_movies() -> list[Movie]:
    """
    returns all movies as list
    """
    return await Movie.find().to_list()


async def get_movies_in_rate_order():
    """

    """
    raise NotImplementedError()


async def pop_movie():
    """
    returns movie that not played yet from top of to_list
    and change movie status to 'in progress'
    or throws HTTPException
    """
    try:
        movies_list = await Movie.find(Movie.status == "not started").sort(
            [(Movie.add_time, pymongo.DESCENDING)]
        ).to_list()
        movie = movies_list[0]
    except IndexError:
        raise HTTPException(
            status_code=400,
            detail="Bad request: no movies to pop"
        )

    movie.status("in progress")
    await movie.save()

    return movie


async def add_movie(movie_data: Movie):
    """
    add new movie to db
    or throws HTTPException if some data incorrect
    """
    validate_status(movie_data.status)
    validate_rate(movie_data.rate)
    validate_status_and_rate(movie_data.status, movie_data.rate)
    validate_status_and_review(movie_data.status, movie_data.review)
    new_movie = Movie(
        name=movie_data.name,
        status=movie_data.status,
        rate=movie_data.rate,
        review=movie_data.review,
        add_time=movie_data.add_time,
        change_time=movie_data.change_time,
        movie_genre=movie_data.movie_genre,
        director=movie_data.director
    )

    return await new_movie.insert()


async def get_movie_by_name(movie_name: str) -> Movie:
    """
    search for movie by it's name
    """
    movie = await Movie.find_one(Movie.name == movie_name)
    if movie is None:
        raise HTTPException(
            status_code=400,
            detail="Bad request: no suck movie"
        )

    return movie


async def remove_movie(movie_name: str):
    """
    removes movie from db
    or throws HTTPException if there's no such movie
    """
    movie = await get_movie_by_name(movie_name)
    return await movie.delete()


async def change_movie_name(movie_name, new_movie_name):
    """
    change movie name
    """
    movie_to_change = await get_movie_by_name(movie_name)
    movie_to_change.name = new_movie_name

    return await movie_to_change.save()


async def change_movie_status(movie_name, new_status):
    """
    change movie status or throws HTTPException
    if status is incorrect
    """
    validate_status(new_status)
    movie_to_change = await get_movie_by_name(movie_name)
    movie_to_change.status = new_status

    return await movie_to_change.save()


async def change_movie_rate(movie_name, new_rate):
    """
    change movie status or throws HTTPException
    if new rate is incorrect
    """
    validate_rate(new_rate)
    movie_to_change = await get_movie_by_name(movie_name)
    validate_status_and_rate(movie_to_change.status, new_rate)
    movie_to_change.rate = new_rate

    return await movie_to_change.save()


async def change_movie_review(movie_name, new_reivew):
    """
    change movie review or throws HTTPException
    """
    movie_to_change = await get_movie_by_name(movie_name)
    validate_status_and_review(movie_to_change.status, new_reivew)
    movie_to_change.review = new_reivew

    return await movie_to_change.save()


async def change_movie_genre(movie_name, new_genre):
    """
    change movie genre
    """
    movie_to_change = await get_movie_by_name(movie_name)
    movie_to_change.movie_genre = new_genre

    return await movie_to_change.save()


async def change_movie_director(movie_name, new_director):
    """
    change movie director
    """
    movie_to_change = await get_movie_by_name(movie_name)
    movie_to_change.director = new_director

    return await movie_to_change.save()
