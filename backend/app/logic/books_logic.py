import pymongo
from pymongo.results import DeleteResult

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


async def get_books_in_rate_order() -> list[Book]:
    """
    returns all books that have rate in descending order
    """
    books_list = await Book.find(
        Book.rate is not None
    ).sort(
        (Book.rate, pymongo.DESCENDING),
    ).to_list()

    return books_list


async def pop_book() -> Book | None:
    """
    returns book that not read yet from top of list
    and change book status to 'in progress' if book exist
    """
    book = await Book.find_one(Book.status == "not started")

    if book is not None:
        book.status = "in progress"
        await book.save()

    return book


async def add_book(book_data: Book) -> Book:
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
        genre=book_data.genre
    )
    return await new_book.insert()


async def get_book_by_name(book_name: str) -> Book | None:
    """
    find book by name and returns it
    """
    book = await Book.find_one(Book.name == book_name)

    return book


async def remove_book(book_name: str) -> None:
    """
    removes book from db
    """
    book = await get_book_by_name(book_name)
    if book is not None:
        await book.delete()
    return None


async def change_book_name(
    book_name: str, new_book_name: str
) -> Book | None:
    """
    change book name
    """
    book = await get_book_by_name(book_name)
    if book is not None:
        book.name = new_book_name
        return await book.save()
    return None


async def change_book_status(
    book_name: str, new_status: str
) -> Book | None:
    """
    change book status
    """
    validate_status(new_status)
    book = await get_book_by_name(book_name)
    if book is not None:
        book.status = new_status
        return await book.save()
    return None


async def change_book_rate(book_name: str, new_rate: int) -> Book | None:
    """
    change book rate
    """
    validate_rate(new_rate)
    book = await get_book_by_name(book_name)
    if book is not None:
        validate_status_and_rate(book.status, new_rate)
        book.rate = new_rate
        return await book.save()
    return None


async def change_book_review(
    book_name: str, new_book_review: str
) -> Book | None:
    """
    change book review
    """
    book = await get_book_by_name(book_name)
    if book is not None:
        validate_status_and_review(book.status, new_book_review)
        book.review = new_book_review
        return await book.save()
    return None


async def change_book_author(
    book_name: str, new_book_author: str
) -> Book | None:
    """
    change book author
    """
    book = await get_book_by_name(book_name)
    if book is not None:
        book.author = new_book_author
        return await book.save()
    return None


async def change_book_genre(
    book_name: str, new_genre: str
) -> Book | None:
    """
    change book genre
    """
    book = await get_book_by_name(book_name)
    if book is not None:
        book.genre = new_genre
        return await book.save()
    return None
