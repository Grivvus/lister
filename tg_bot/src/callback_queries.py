from aiogram.types import CallbackQuery

from requests_ import (
    book_requests,
    game_requests,
    movie_requests,
)
import utils


# start book segment
async def add_book_query(callback: CallbackQuery): ...


async def change_book_query(callback: CallbackQuery): ...


async def remove_book_query(callback: CallbackQuery):
    response = await book_requests.remove_instance()
    response_text = utils.response_to_text(response)
    await callback.message.answer(response_text)


async def get_all_books_query(callback: CallbackQuery):
    response = await book_requests.get_all_books()
    response_text = utils.response_to_text(response)
    await callback.message.answer(response_text)


async def get_book_in_rate_order(callback: CallbackQuery):
    response = await book_requests.get_instance_in_rate_order()
    response_text = utils.response_to_text(response)
    await callback.message.answer(response_text)


async def pop_book_query(callback: CallbackQuery):
    response = await book_requests.pop_instance()
    response_text = utils.response_to_text(response)
    await callback.message.answer(response_text)


# start game segment
async def add_game_query(callback: CallbackQuery): ...


async def change_game_query(callback: CallbackQuery): ...


async def remove_game_query(callback: CallbackQuery): ...


async def get_all_game_query(callback: CallbackQuery): ...


async def pop_game_query(callback: CallbackQuery): ...


# start movie segment
async def add_movie_query(callback: CallbackQuery): ...


async def change_movie_query(callback: CallbackQuery): ...


async def remove_movie_query(callback: CallbackQuery): ...


async def get_all_movie_query(callback: CallbackQuery): ...


async def pop_movie_query(callback: CallbackQuery): ...
