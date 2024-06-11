import pymongo

from app.models import Book


async def get_all_books():
    books_list = await Book.find().to_list()

    return books_list


async def pop_book():
    books_list = await Book.find(Book.status == "not started").sort(
        [(Book.add_time, pymongo.DESCENDING)]
    ).to_list()

    return books_list[0]


async def add_book(book_data: Book):
    new_book = Book(
        name=book_data.name,
        user=book_data.user,
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
    await Book.find_one(Book.name == book_name).delete()


async def change_book():
    raise NotImplementedError()
