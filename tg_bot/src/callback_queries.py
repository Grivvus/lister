from aiogram.types import CallbackQuery
from aiogram.fsm.context import FSMContext

import fsm
from requests_ import (
    book_requests,
    game_requests,
    movie_requests,
)
import utils


# start book segment
async def add_book_query(callback: CallbackQuery, state: FSMContext):
    await state.set_state(fsm.BookEnterState.enter_name)
    await callback.message.answer(
        "Добавьте все необходимые данные для добавления книги"
    )
    await callback.message.answer("Введите название книги:")


async def remove_book_query(callback: CallbackQuery, state: FSMContext):
    await state.set_state(fsm.BookDeleteState.enter_name)
    await callback.message.answer(
        "Введите название книги, которую хотите удалить:"
    )


async def get_all_books_query(callback: CallbackQuery):
    response = book_requests.get_all_instance()
    response_text = utils.response_to_text(response)
    await callback.message.answer(response_text)


async def get_books_in_rate_order(callback: CallbackQuery):
    response = book_requests.get_instance_in_rate_order()
    response_text = utils.response_to_text(response)
    await callback.message.answer(response_text)


async def pop_book_query(callback: CallbackQuery):
    response = book_requests.pop_instance()
    response_text = utils.response_to_text(response)
    await callback.message.answer(response_text)


# start game segment
async def add_game_query(callback: CallbackQuery, state: FSMContext):
    await state.set_state(fsm.GameEnterState.enter_name)
    await callback.message.answer(
        "Добавьте все необходимые данные для добавления игры"
    )
    await callback.message.answer("Введите название игры:")


async def remove_game_query(callback: CallbackQuery, state: FSMContext):
    await state.set_state(fsm.GameDeleteState.enter_name)
    await callback.message.answer(
        "Введите название игры, которую хотите удалить:"
    )


async def get_all_games_query(callback: CallbackQuery):
    response = game_requests.get_all_instance()
    response_text = utils.response_to_text(response)
    await callback.message.answer(response_text)


async def get_games_in_rate_order(callback: CallbackQuery):
    response = game_requests.get_instance_in_rate_order()
    response_text = utils.response_to_text(response)
    await callback.message.answer(response_text)


async def pop_game_query(callback: CallbackQuery):
    response = game_requests.pop_instance()
    response_text = utils.response_to_text(response)
    await callback.message.answer(response_text)


# start movie segment
async def add_movie_query(callback: CallbackQuery, state: FSMContext):
    await state.set_state(fsm.MovieEnterState.enter_name)
    await callback.message.answer(
        "Добавьте все необходимые данные для добавления фильма"
    )
    await callback.message.answer("Введите название фильмы:")


async def remove_movie_query(callback: CallbackQuery, state: FSMContext):
    await state.set_state(fsm.MovieDeleteState.enter_name)
    await callback.message.answer(
        "Введите название фильмы, который хотите удалить:"
    )


async def get_all_movies_query(callback: CallbackQuery):
    response = movie_requests.get_all_instance()
    response_text = utils.response_to_text(response)
    await callback.message.answer(response_text)


async def get_movies_in_rate_order(callback: CallbackQuery):
    response = movie_requests.get_instance_in_rate_order()
    response_text = utils.response_to_text(response)
    await callback.message.answer(response_text)


async def pop_movie_query(callback: CallbackQuery):
    response = movie_requests.pop_instance()
    response_text = utils.response_to_text(response)
    await callback.message.answer(response_text)
