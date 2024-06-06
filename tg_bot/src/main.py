import asyncio
import logging
import sys

from aiogram import Bot, Dispatcher, F
from aiogram.filters import Command
from aiogram.types import Message, CallbackQuery

from constants import WELCOME_TEXT, HELP_TEXT
from callback_queries import *
from keyboards import make_kb_for_start, get_first_level_inline_keyboard
from settings import settings

dp = Dispatcher()


@dp.message(Command("start", ignore_case=True))
async def start_handler(message: Message):
    """
    print welcom message and help text in user chat
    """

    await message.answer(text=WELCOME_TEXT)
    await message.answer(
        "what's your target", reply_markup=make_kb_for_start()
    )


@dp.message(Command("help", ignore_case=True))
async def command_start_handler(message: Message):
    """
    print help texte in user chat
    """

    await message.answer(text=HELP_TEXT)


@dp.message(Command("books", ignore_case=True))
async def books_handler(message: Message):
    """
    docs will be here
    """
    builder_kb = get_first_level_inline_keyboard("books")

    await message.answer(
        "Какое действие вы хотите произвести?",
        reply_markup=builder_kb.as_markup()
    )


@dp.message(Command("games", ignore_case=True))
async def games_handler(message: Message):
    """
    docs will be here
    """
    builder_kb = get_first_level_inline_keyboard("games")

    await message.answer(
        "Какое действие вы хотите произвести?",
        reply_markup=builder_kb.as_markup()
    )


@dp.message(Command("movies", ignore_case=True))
async def movies_handler(message: Message):
    """
    docs will be here
    """
    builder_kb = get_first_level_inline_keyboard("movies")

    await message.answer(
        "Какое действие вы хотите произвести?",
        reply_markup=builder_kb.as_markup()
    )


@dp.callback_query(F.data.endswith("book"))
async def book_query_handler(callback: CallbackQuery):
    if callback.data.startswith("add"):
        add_book_query(callback)
    elif callback.data.startswith("change"):
        change_book_query(callback)
    elif callback.data.startswith("del"):
        del_book_query(callback)
    elif callback.data.startswith("read_all"):
        read_all_book_query(callback)
    elif callback.data.startswith("pop"):
        pop_book_query(callback)
    else:
        await callback.message.edit_text("unkown command")

    await callback.answer()


@dp.callback_query(F.data.endswith("game"))
async def game_query_handler(callback: CallbackQuery):
    if callback.data.startswith("add"):
        add_game_query(callback)
    elif callback.data.startswith("change"):
        change_game_query(callback)
    elif callback.data.startswith("del"):
        del_game_query(callback)
    elif callback.data.startswith("read_all"):
        read_all_game_query(callback)
    elif callback.data.startswith("pop"):
        pop_game_query(callback)
    else:
        await callback.message.edit_text("unkown command")

    await callback.answer()


@dp.callback_query(F.data.endswith("movie"))
async def movie_query_handler(callback: CallbackQuery):
    if callback.data.startswith("add"):
        add_movie_query(callback)
    elif callback.data.startswith("change"):
        change_movie_query(callback)
    elif callback.data.startswith("del"):
        del_movie_query(callback)
    elif callback.data.startswith("read_all"):
        read_all_movie_query(callback)
    elif callback.data.startswith("pop"):
        pop_movie_query(callback)
    else:
        await callback.message.edit_text("unkown command")

    await callback.answer()


async def main():
    bot = Bot(settings.BOT_TOKEN)

    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
