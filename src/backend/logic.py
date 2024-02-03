"""all logic for views from app.py"""

from sqlalchemy import select

from models import Game, Book, Movie
from db_utils import DBStuff

stuff: DBStuff = DBStuff()


def get_games_list(user_id: int) -> dict:
    """query to db to fetch all games in order of addition"""
    games_dict = {}
    with stuff.create_session() as session:
        games = select(Game).where(Game.user_id==user_id)\
            .order_by(Game.added_at)
        for game in session.scalars(games):
            games_dict[game.title] = game

    return games_dict


def get_books_list(user_id: int) -> dict:
    """query to db to fetch all books in order of addition"""
    books_dict = {}
    with stuff.create_session() as session:
        books = select(Book).where(Book.user_id==user_id)\
            .order_by(Book.added_at)
        for book in session.scalars(books):
            books_dict[book.title] = book

    return books_dict


def get_movies_list(user_id: int) -> dict:
    """query to db to fetch all movies in order of addition"""
    movies_dict = {}
    with stuff.create_session() as session:
        movies = select(Movie).where(Movie.user_id==user_id)\
            .order_by(Movie.added_at)
        for movie in session.scalars(movies):
            movies_dict[movie.title] = movie

    return movies_dict


def pop_game(user_id: int) -> dict:
    with stuff.create_session() as session:
        game = select(Game).where(Game.user_id==user_id)\
            .order_by(Game.priority, Game.added_at).limit(1)
        game = session.scalar(game)

        return {game.title: game}

def pop_book(user_id: int) -> dict:
    with stuff.create_session() as session:
        book = select(Book).where(Book.user_id==user_id)\
            .order_by(Book.priority, Book.added_at).limit(1)
        book = session.scalar(book)

        return {book.title: book}

def pop_movie(user_id: int) -> dict:
    with stuff.create_session() as session:
        movie = select(Movie).where(Movie.user_id==user_id)\
            .order_by(Movie.priority, Movie.added_at).limit(1)
        movie = session.scalar(movie)

        return {movie.title: movie}


def add_game(
        user_id: int,
        title: str,
        link: str | None,
        priority: int = 3,
) -> None:
    """add new game to the db"""
    new_game = Game(
        user_id=user_id, title=title,
        link=link, priority = priority,
    )
    with stuff.create_session() as session:
        session.add(new_game)
        session.commit()

def add_book(
        user_id: int,
        title: str,
        author: str | None,
        link: str | None,
        priority: int = 3,
) -> None:
    """add new book to the db"""
    new_book = Book(
        user_id=user_id, title=title,
        author=author, link=link, priority=priority
    )
    with stuff.create_session() as session:
        session.add(new_book)
        session.commit()

def add_movie(
        user_id: int,
        title: str,
        link: str | None,
        priority: int = 3
) -> None:
    """add new movie to the db"""
    new_movie = Movie(
        user_id=user_id, title=title,
        link=link, priority=priority
    )
    with stuff.create_session() as session:
        session.add(new_movie)
        session.commit()


def change_game_status():
    """
    automaticly call when person pop any game from list of games
    and change status of the game and taken_at in db
    """
    raise NotImplementedError()
