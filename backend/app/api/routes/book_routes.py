from fastapi import APIRouter

from app.models import Book, Game, Movie
from app.logic import books_logic


router = APIRouter()


@router.get("/")
def get_all_books():
    """
    returns all books
    """
    return books_logic.get_all_books()


@router.get("/get_books_in_rate_order")
def get_books_in_rate_order():
    """
    returns all books in decreasing order of rate
    """
    raise NotImplementedError("not done yet")


@router.get("/pop_book")
def pop_book():
    """
    returns book with highest rate that not read yet
    """
    return books_logic.pop_book()


@router.post("/add_book")
def add_book(book_data: Book):
    """
    add new book to db
    """
    return books_logic.add_book(book_data)


@router.delete("/remove_book/{book_name}")
def remove_book(book_name: str):
    """
    removing book by name
    """
    return books_logic(book_name)


@router.put("/change_book")
def change_book():
    """
    changing book fields (identifying by name)
    """
    return books_logic.change_book()
