from typing import Annotated

from fastapi import APIRouter, Body, Path

from app.models import Book
from app.logic import books_logic


router = APIRouter()


@router.get("/get_all_books")
async def get_all_books() -> list[Book]:
    """
    returns all books
    """
    return await books_logic.get_all_books()


@router.get("/get_books_in_rate_order")
async def get_books_in_rate_order() -> list[Book]:
    """
    returns all books where rate is not None
    in decreasing order of rate
    """
    return await books_logic.get_books_in_rate_order()


@router.get("/pop_book")
async def pop_book() -> Book | None:
    """
    returns book with highest rate that not read yet
    and change it status to 'in progress'
    or raises HTTPExcetion with status code 400 is book is None
    """
    return await books_logic.pop_book()


@router.post("/add_book")
async def add_book(book_data: Book = Body(embed=True)) -> Book | None:
    """
    add new book to db or raises HTTPExcetion
    with status_code 422
    """
    print(book_data)
    return await books_logic.add_book(book_data)


@router.delete("/remove_book/{book_name}",)
async def remove_book(book_name: str):
    """
    removing book by name or raises HTTPExcetion
    with status_code 400 if book is None
    """
    return await books_logic.remove_book(book_name)


@router.patch("/change_book_name/{book_name}")
async def change_book_name(
    book_name: Annotated[str, Path()],
    new_book_name: Annotated[str, Body()]
) -> Book | None:
    """
    change book_name or raises HTTPExcetion with
    status_code 400 if book is None
    """
    return await books_logic.change_book_name(book_name, new_book_name)


@router.patch("/change_book_status/{book_name}")
async def change_book_status(
    book_name: Annotated[str, Path()],
    new_book_status: Annotated[str, Body()]
) -> Book | None:
    """
    change book_status or raises HTTPExcetion with
    status_code 400 if book is None
    or raises HTTPExcetion with status_code 422
    """
    return await books_logic.change_book_status(book_name, new_book_status)


@router.patch("/change_book_rate/{book_name}")
async def change_book_rate(
    book_name: Annotated[str, Path()],
    new_book_rate: Annotated[int, Body()]
) -> Book | None:
    """
    change book_rate
    or raises HTTPExcetion with status_code 400 if book is None
    or raises HTTPExcetion with status_code 422
    """
    return await books_logic.change_book_rate(book_name, new_book_rate)


@router.patch("/change_book_review{book_name}")
async def change_book_review(
    book_name: Annotated[str, Path()],
    new_book_review: Annotated[str, Body()]
) -> Book | None:
    """
    change book_review or raises HTTPExcetion with
    status_code 400 if book is None
    """
    return await books_logic.change_book_review(
        book_name, new_book_review
    )


@router.patch("/change_book_author/{book_name}")
async def change_book_author(
    book_name: Annotated[str, Path()],
    new_book_author: Annotated[str, Body()]
) -> Book | None:
    """
    change book_author or raises HTTPExcetion with
    status_code 400 if book is None
    """
    return await books_logic.change_book_author(book_name, new_book_author)


@router.patch("/change_book_genre/{book_name}")
async def change_book_genre(
    book_name: Annotated[str, Path()],
    new_book_genre: Annotated[str, Body()]
) -> Book | None:
    """
    change book_genre or raises HTTPExcetion with
    status_code 400 if book is None
    """
    return await books_logic.change_book_genre(book_name, new_book_genre)
