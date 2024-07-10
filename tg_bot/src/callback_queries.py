from aiogram.types import CallbackQuery

import requests_
import utils


# start book segment
async def add_book_query(callback: CallbackQuery):
    ...


async def change_book_query(callback: CallbackQuery):
    ...


async def del_book_query(callback: CallbackQuery):
    ...


async def get_all_books_query(callback: CallbackQuery):
    response: list[dict] = await requests_.get_all_books()
    response_text = utils.response_to_text(response)
    await callback.message.answer(response_text)


async def pop_book_query(callback: CallbackQuery):
    ...


# start game segment
async def add_game_query(callback: CallbackQuery):
    ...


async def change_game_query(callback: CallbackQuery):
    ...


async def del_game_query(callback: CallbackQuery):
    ...


async def get_all_game_query(callback: CallbackQuery):
    ...


async def pop_game_query(callback: CallbackQuery):
    ...


# start movie segment
async def add_movie_query(callback: CallbackQuery):
    ...


async def change_movie_query(callback: CallbackQuery):
    ...


async def del_movie_query(callback: CallbackQuery):
    ...


async def get_all_movie_query(callback: CallbackQuery):
    ...


async def pop_movie_query(callback: CallbackQuery):
    ...
