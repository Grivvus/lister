from fastapi import HTTPException
import pymongo

from app.models import Book
from app.logic.validation import (
    validate_rate,
    validate_status,
    validate_status_and_rate
)


async def get_all_books() -> list[Book]:
    """
    returns all books as list
    """
    books_list = await Book.find().to_list()

    return books_list


async def pop_book():
    """
    returns book that not read yet from top of list
    and change book status to 'in progress'
    or throws HTTPException
    """
    try:
        books_list = await Book.find(Book.status == "not started").sort(
            [(Book.add_time, pymongo.DESCENDING)]
        ).to_list()
        book = books_list[0]
    except IndexError:
        raise HTTPException(status_code=400, detail="no books to pop")

    book.status = "in progress"
    book.save()

    return book


async def add_book(book_data: Book):
    """
    add new book to db
    or throws HTTPException if some data is incorrect
    """
    if not validate_status(book_data.status):
        raise HTTPException(status_code=422, detail="wrong status")
    if not validate_rate(book_data.rate):
        raise HTTPException(status_code=422, detail="wrong rate")
    if not validate_status_and_rate(book_data.status, book_data.rate):
        raise HTTPException(
            status_code=422,
            detailt="you cannot rate book if you not finished it yet"
        )
    new_book = Book(
        name=book_data.name,
        status=book_data.status,
        rate=book_data.rate,
        review=book_data.review,
        add_time=book_data.add_time,
        change_time=book_data.change_time,
        author=book_data.author,
        book_genre=book_data.book_genre
    )
    return await new_book.insert()


async def remove_book(book_name: str):
    """
    removes book from db or throws HTTPException if something goes wrong
    """
    try:
        await Book.find_one(Book.name == book_name).delete()
    except Exception as e:
        raise HTTPException(
            status_code=400,
            detail=f"cannot remove book: exception {e}"
        )


async def get_book_by_name(book_name: str):
    """
    find book by name and returns it
    """
    return await Book.find_one(Book.name == book_name)


async def change_book_status(book_name: str, new_status: str):
    """
    change book status or throws HTTPException
    if new status is incorrect
    """
    validation_res = validate_status(new_status)
    if not validation_res:
        raise HTTPException(status_code=400, detail="wrong status")
    else:
        book_to_change = await get_book_by_name(book_name)
        book_to_change.status = new_status

        return await book_to_change.save()


async def change_book_rate(book_name: str, new_rate: int):
    """
    change book rate or throws HTTPException
    if new rate is incorrect
    """
    validation_res = validate_rate(new_rate)
    if not validation_res:
        raise HTTPException(status_code=400, detail="wrong rate")
    else:
        book_to_change = await get_book_by_name(book_name)
        book_to_change.rate = new_rate

        return await book_to_change.save()
