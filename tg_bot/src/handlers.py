from aiogram import Router, F
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import default_state
from aiogram.filters import Command, StateFilter
from aiogram.types import Message, CallbackQuery

import callback_queries
import fsm
from constants import WELCOME_TEXT, HELP_TEXT
from keyboards import (
    make_kb_for_start, get_first_level_inline_keyboard,
    get_possible_statuses_keyboard, get_possible_rate
)
from requests_ import book_requests
import utils

r = Router()


@r.message(Command("start", ignore_case=True))
async def start_handler(message: Message):
    """
    print welcom message and help text in user chat
    """

    await message.answer(text=WELCOME_TEXT)
    await message.answer(
        "what's your target", reply_markup=make_kb_for_start()
    )


@r.message(Command("help", ignore_case=True))
async def command_start_handler(message: Message):
    """
    print help texte in user chat
    """

    await message.answer(text=HELP_TEXT)


@r.message(Command("clear"))
async def clear_state(message: Message, state: FSMContext):
    await state.clear()
    await message.answer("Состояние сброшено")


@r.message(Command("books", ignore_case=True))
async def books_handler(message: Message):
    """
    docs will be here
    """
    builder_kb = get_first_level_inline_keyboard("books")

    await message.answer(
        "Какое действие вы хотите произвести?",
        reply_markup=builder_kb.as_markup()
    )


@r.message(Command("games", ignore_case=True))
async def games_handler(message: Message):
    """
    docs will be here
    """
    builder_kb = get_first_level_inline_keyboard("games")

    await message.answer(
        "Какое действие вы хотите произвести?",
        reply_markup=builder_kb.as_markup()
    )


@r.message(Command("movies", ignore_case=True))
async def movies_handler(message: Message):
    """
    docs will be here
    """
    builder_kb = get_first_level_inline_keyboard("movies")

    await message.answer(
        "Какое действие вы хотите произвести?",
        reply_markup=builder_kb.as_markup()
    )


@r.callback_query(F.data.endswith("books"))
async def book_query_handler(callback: CallbackQuery, state: FSMContext):
    if callback.data.startswith("add"):
        await callback_queries.add_book_query(callback, state)
    if callback.data.startswith("del"):
        await callback_queries.remove_book_query(callback, state)
    elif callback.data.startswith("get_all"):
        await callback_queries.get_all_books_query(callback)
    elif callback.data.startswith("pop"):
        await callback_queries.pop_book_query(callback)
    else:
        callback.message.edit_text("unkown command")

    await callback.answer("response is over")


@r.callback_query(F.data.endswith("games"))
async def game_query_handler(callback: CallbackQuery):
    if callback.data.startswith("add"):
        await callback_queries.add_game_query(callback)
    elif callback.data.startswith("del"):
        await callback_queries.remove_game_query(callback)
    elif callback.data.startswith("get_all"):
        await callback_queries.get_all_game_query(callback)
    elif callback.data.startswith("pop"):
        await callback_queries.pop_game_query(callback)
    else:
        await callback.message.edit_text("unkown command")

    await callback.answer()


@r.callback_query(F.data.endswith("movies"))
async def movie_query_handler(callback: CallbackQuery):
    if callback.data.startswith("add"):
        await callback_queries.add_movie_query(callback)
    elif callback.data.startswith("del"):
        await callback_queries.remove_movie_query(callback)
    elif callback.data.startswith("get_all"):
        await callback_queries.get_all_movie_query(callback)
    elif callback.data.startswith("pop"):
        await callback_queries.pop_movie_query(callback)
    else:
        await callback.message.edit_text("unkown command")

    await callback.answer()


@r.message(fsm.BookEnterState.enter_name)
async def add_book_author(message: Message, state: FSMContext):
    await state.update_data(name=message.text)
    await message.answer("Отлично, теперь введи автора книги")
    await state.set_state(fsm.BookEnterState.enter_author)


@r.message(fsm.BookEnterState.enter_author)
async def add_book_genre(message: Message, state: FSMContext):
    await state.update_data(author=message.text)
    await message.answer("Так, теперь время ввести жанр книги")
    await message.answer(
        "Если ты не знаешь жанр, просто отправь '-'"
    )
    await state.set_state(fsm.BookEnterState.enter_genre)


@r.message(fsm.BookEnterState.enter_genre)
async def add_book_status(message: Message, state: FSMContext):
    await state.update_data(book_genre=message.text.lower())
    await message.answer(
        "отлично, теперь выбери статус книги",
        reply_markup=get_possible_statuses_keyboard(),
    )
    await state.set_state(fsm.BookEnterState.enter_status)


@r.message(
    fsm.BookEnterState.enter_status,
    F.text.in_(["not started", "in progress"])
)
async def add_book_finished_state(message: Message, state: FSMContext):
    await state.update_data(status=message.text)
    await message.answer("значит больше данных от тебя не требуется")

    current_data = await state.get_data()
    final_data = utils.prepair_insert_data_to_request(current_data)
    if book_requests.add_instance(final_data) is not None:
        await message.answer("Вы добавили книгу:")
        await message.answer(final_data.__str__())
    else:
        await message.answer("Что-то пошло не так")

    await state.clear()


@r.message(
    fsm.BookEnterState.enter_status,
    F.text.in_(["finished"])
)
async def add_book_rate(message: Message, state: FSMContext):
    await state.update_data(status=message.text)
    await message.answer("значит надо еще добавить некоторые данные")
    await message.answer(
        "какую бы вы оценку поставили книге (от 0 до 10)",
        reply_markup=get_possible_rate()
    )
    await state.set_state(fsm.BookEnterState.enter_rate)


@r.message(fsm.BookEnterState.enter_rate)
async def add_book_review(message: Message, state: FSMContext):
    await state.update_data(rate=message.text)
    await state.set_state(fsm.BookEnterState.enter_review)
    await message.answer("Напишите небольшой отзыв на эту книгу")


@r.message(fsm.BookEnterState.enter_review)
async def mark_book_as_ready(message: Message, state: FSMContext):
    await state.update_data(review=message.text)

    current_data = await state.get_data()
    final_data = utils.prepair_insert_data_to_request(current_data)
    if book_requests.add_instance(final_data) is not None:
        await message.answer("Вы добавили книгу:")
        await message.answer(final_data.__str__())
    else:
        await message.answer("Что-то пошло не так")

    await state.clear()


@r.message(fsm.BookDeleteState.enter_name)
async def delete_book(message: Message, state: FSMContext):
    if book_requests.remove_instance(message.text):
        await message.answer("Книга успешно удалена")
    else:
        await message.answer(
            "Не удалось удалить книгу, проверьте корректность имени"
        )
    await state.clear()
