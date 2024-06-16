from fastapi import HTTPException
import pymongo

from app.models import Book
from app.logic.validation import (
    validate_rate,
    validate_status,
    validate_status_and_rate,
    validate_status_and_review
)


async def get_all_books() -> list[Book]:
    """
    returns all books as list
    """
    books_list = await Book.find().to_list()

    return books_list


async def get_books_in_rate_order():
    """

    """
    raise NotImplementedError()


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
        # could probably return None, not raise exception
        raise HTTPException(
            status_code=400,
            detail="Bad request: no books to pop"
        )

    book.status = "in progress"
    await book.save()

    return book


async def add_book(book_data: Book):
    """
    add new book to db
    or throws HTTPException if some data is incorrect
    """
    validate_rate(book_data.rate)
    validate_status(book_data.status)
    validate_status_and_rate(book_data.status, book_data.rate)
    validate_status_and_review(book_data.status, book_data.review)
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
    book = await Book.find_one(Book.name == book_name)
    if book is not None:
        await book.delete()
    else:
        raise HTTPException(
            status_code=400,
            detail="Bad request: wrong book name"
        )


async def get_book_by_name(book_name: str):
    """
    find book by name and returns it
    """
    book = await Book.find_one(Book.name == book_name)
    if book is None:
        raise HTTPException(
            status_code=400,
            detail="Bad request: no such book"
        )

    return book


async def change_book_name(book_name: str, new_book_name: str):
    """

    """
    book_to_change = await get_book_by_name(book_name)
    book_to_change.name = new_book_name

    return await book_to_change.save()


async def change_book_status(book_name: str, new_status: str):
    """
    change book status or throws HTTPException
    if new status is incorrect
    """
    validate_status(new_status)
    book_to_change = await get_book_by_name(book_name)
    book_to_change.status = new_status

    return await book_to_change.save()


async def change_book_rate(book_name: str, new_rate: int):
    """
    change book rate or throws HTTPException
    if new rate is incorrect
    """
    validate_rate(new_rate)
    book_to_change = await get_book_by_name(book_name)
    validate_status_and_rate(book_to_change.status, new_rate)
    book_to_change.rate = new_rate

    return await book_to_change.save()


async def change_book_review(book_name: str, new_book_review: str):
    """

    """
    book_to_change = await get_book_by_name(book_name)
    validate_status_and_review(book_to_change.status, new_book_review)
    book_to_change.review = new_book_review

    return await book_to_change.save()


async def change_book_author(book_name: str, new_book_author: str):
    """

    """
    book_to_change = await get_book_by_name(book_name)
    book_to_change.author = new_book_author

    return await book_to_change.save()


async def change_book_genre(book_name: str, new_book_genre: str):
    """

    """
    book_to_change = await get_book_by_name(book_name)
    book_to_change.book_genre = new_book_genre

    return await book_to_change.save()
