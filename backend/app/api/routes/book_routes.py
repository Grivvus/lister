from fastapi import APIRouter, Body, status

from app.models import Book
from app.logic import books_logic


router = APIRouter()


@router.get("/")
async def get_all_books():
    """
    returns all books
    """
    return await books_logic.get_all_books()


@router.get("/get_books_in_rate_order")
def get_books_in_rate_order():
    """
    returns all books in decreasing order of rate
    """
    raise NotImplementedError("not done yet")


@router.get("/pop_book")
async def pop_book():
    """
    returns book with highest rate that not read yet
    """
    return await books_logic.pop_book()


@router.post("/add_book")
async def add_book(book_data: Book = Body(embed=True)):
    """
    add new book to db
    """
    print(book_data)
    return await books_logic.add_book(book_data)


@router.delete(
    "/remove_book/{book_name}", status_code=status.HTTP_202_ACCEPTED
)
async def remove_book(book_name: str):
    """
    removing book by name
    """
    return await books_logic.remove_book(book_name)


@router.patch("/change_book/{book_name}")
async def change_book(book_name: str):
    """
    changing book fields (identifying by name)
    """
    raise NotImplementedError("not done yet")
