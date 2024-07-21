import pymongo
from pymongo.results import DeleteResult

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


async def get_movies_in_rate_order() -> list[Movie]:
    """
    returns list of movies that had rate in descending order
    """
    movies_list = await Movie.find(
        Movie.rate is not None
    ).sort(
        (Movie.rate, pymongo.DESCENDING)
    ).to_list()

    return movies_list


async def pop_movie() -> Movie | None:
    """
    returns movie that not played yet from top of to_list
    and change movie status to 'in progress' if movie exist
    """
    movie = await Movie.find_one(Movie.status == "not started")
    if movie is not None:
        movie.status("in progress")
        await movie.save()
    return movie


async def add_movie(movie_data: Movie) -> Movie:
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


async def get_movie_by_name(movie_name: str) -> Movie | None:
    """
    search for movie by it's name
    """
    movie = await Movie.find_one(Movie.name == movie_name)
    return movie


async def remove_movie(movie_name: str) -> None:
    """
    removes movie from db
    or throws HTTPException if there's no such movie
    """
    movie = await get_movie_by_name(movie_name)
    if movie is not None:
        await movie.delete()
    return None


async def change_movie_name(
    movie_name: str, new_movie_name: str
) -> Movie | None:
    """
    change movie name
    """
    movie = await get_movie_by_name(movie_name)
    if movie is not None:
        movie.name = new_movie_name
        return await movie.save()
    return None


async def change_movie_status(
    movie_name: str, new_status: str
) -> Movie | None:
    """
    change movie status or throws HTTPException
    if status is incorrect
    """
    validate_status(new_status)
    movie = await get_movie_by_name(movie_name)
    if movie is not None:
        movie.status = new_status
        return await movie.save()
    return None


async def change_movie_rate(movie_name: str, new_rate: int) -> Movie | None:
    """
    change movie status or throws HTTPException
    if new rate is incorrect
    """
    validate_rate(new_rate)
    movie = await get_movie_by_name(movie_name)
    if movie is not None:
        validate_status_and_rate(movie.status, new_rate)
        movie.rate = new_rate
        return await movie.save()
    return None


async def change_movie_review(
    movie_name: str, new_reivew: str
) -> Movie | None:
    """
    change movie review
    """
    movie = await get_movie_by_name(movie_name)
    if movie is not None:
        validate_status_and_review(movie.status, new_reivew)
        movie.review = new_reivew
        return await movie.save()
    return None


async def change_movie_genre(movie_name: str, new_genre: str) -> Movie | None:
    """
    change movie genre
    """
    movie = await get_movie_by_name(movie_name)
    if movie is not None:
        movie.movie_genre = new_genre
        return await movie.save()
    return None


async def change_movie_director(
    movie_name: str, new_director: str
) -> Movie | None:
    """
    change movie director
    """
    movie = await get_movie_by_name(movie_name)
    if movie is not None:
        movie.director = new_director
        return await movie.save()
    return None
