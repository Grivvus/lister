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
            .order_by(Game.priority, Game.added_at)
        for game in session.scalars(games):
            games_dict[game.title] = game

    return games_dict

def get_books_list(user_id: int) -> dict:
    """query to db to fetch all books in order of addition"""
    books_dict = {}
    with stuff.create_session() as session:
        books = select(Book).where(Book.user_id==user_id)\
            .order_by(Book.priority, Book.added_at)
        for book in session.scalars(books):
            books_dict[book.title] = book

    return books_dict

def get_movies_list(user_id: int) -> dict:
    """query to db to fetch all movies in order of addition"""
    movies_dict = {}
    with stuff.create_session() as session:
        movies = select(Movie).where(Movie.user_id==user_id)\
            .order_by(Movie.priority, Movie.added_at)
        for movie in session.scalars(movies):
            movies_dict[movie.title] = movie

    return movies_dict


def pop_game(user_id: int) -> dict:
    with stuff.create_session() as session:
        game = select(Game).where(Game.user_id==user_id)\
            .wher(Game.status=="o").order_by(Game.priority, Game.added_at)\
            .limit(1)
        game = session.scalar(game)
        change_game_status(game.id, "p")
        return {game.title: game}

def pop_book(user_id: int) -> dict:
    with stuff.create_session() as session:
        book = select(Book).where(Book.user_id==user_id)\
            .where(Book.status=="o").order_by(Book.priority, Book.added_at)\
            .limit(1)
        book = session.scalar(book)
        change_book_status(book.id, "p")
        return {book.title: book}

def pop_movie(user_id: int) -> dict:
    with stuff.create_session() as session:
        movie = select(Movie).where(Movie.user_id==user_id)\
            .where(Movie.status=="o").order_by(Movie.priority, Movie.added_at)\
            .limit(1)
        movie = session.scalar(movie)
        change_movie_status(movie.id, "p")
        return {movie.title: movie}


def change_book_status(book_id: int, new_status: str):
    validate_status(new_status)
    with stuff.create_session() as session:
        session.query(Book).filter(Book.id==book_id).\
        update({Book.status: new_status})
        session.commit()

def change_game_status(game_id: int, new_status: str):
    validate_status(new_status)
    with stuff.create_session() as session:
        session.query(Game).filter(Game.id==game_id).\
        update({Game.status: new_status})
        session.commit()

def change_movie_status(movie_id: int, new_status: str):
    validate_status(new_status)
    with stuff.create_session() as session:
        session.query(Movie).filter(Movie.id==movie_id).\
        update({Movie.status: new_status})
        session.commit()


def change_game_priority(game_id: int, new_priority: int):
    with stuff.create_session() as session:
        session.query(Game).filter(Game.id==game_id).\
        update({Game.priority: new_priority})
        session.commit()

def change_book_priority(book_id: int, new_priority: int):
    with stuff.create_session() as session:
        session.query(Book).filter(Book.id==book_id).\
        update({Book.priority: new_priority})
        session.commit()

def change_movie_priority(movie_id: int, new_priority: int):
    with stuff.create_session() as session:
        session.query(Movie).filter(Movie.id==movie_id).\
        update({Movie.priority: new_priority})
        session.commit()


def validate_status(status: str) -> None:
    if status not in ["o", "c", "p"]:
        raise ValueError("Статус объекта задан не правильно")

def validate_priority(priority: int) -> None:
    if priority not in range(1, 4):
        raise ValueError("Проиритет объектов задан не правильно")


def add_game(
        user_id: int,
        title: str,
        link: str | None,
        priority: int = 3,
        status: str = "o",
) -> None:
    """add new game to the db"""
    validate_priority(priority)
    validate_status(status)
    new_game = Game(
        user_id=user_id, title=title,
        link=link, priority=priority, status=status
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
        status: str = "o",
) -> None:
    """add new book to the db"""
    validate_priority(priority)
    validate_status(status)
    new_book = Book(
        user_id=user_id, title=title, author=author,
        link=link, priority=priority, status=status
    )
    with stuff.create_session() as session:
        session.add(new_book)
        session.commit()

def add_movie(
        user_id: int,
        title: str,
        link: str | None,
        priority: int = 3,
        status: str = "o",
) -> None:
    """add new movie to the db"""
    validate_priority(priority)
    validate_status(status)
    new_movie = Movie(
        user_id=user_id, title=title,
        link=link, priority=priority, status=status
    )
    with stuff.create_session() as session:
        session.add(new_movie)
        session.commit()

def delete_game(game_id: int):
    """deleting game by id from db"""
    with stuff.create_session() as session:
        session.query(Game).filter(Game.id==game_id).delete()

def delete_book(book_id: int):
    """deleting book by id from db"""
    with stuff.create_session() as session:
        session.query(Book).filter(Book.id==book_id).delete()

def delete_movie(movie_id: int):
    """deleting movie by id from db"""
    with stuff.create_session() as session:
        session.query(Movie).filter(Movie.id==movie_id).delete()


def check_for_book_permition(user_id: int, book_id: int) -> bool:
    with stuff.create_session() as session:
        book: Book = session.query(Book).get(book_id)
        return book.user_id == user_id

def check_for_game_permition(user_id: int, game_id: int) -> bool:
    with stuff.create_session() as session:
        game: Game = session.query(Game).get(game_id)
        return game.user_id == user_id

def check_for_movie_permition(user_id: int, movie_id: int) -> bool:
    with stuff.create_session() as session:
        movie: Movie = session.query(Movie).get(movie_id)
        return movie.user_id == user_id
