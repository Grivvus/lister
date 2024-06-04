import asyncio
import logging
import sys

from aiogram import Bot, Dispatcher
from aiogram.filters import Command
from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton

from constants import WELCOME_TEXT, HELP_TEXT
from settings import settings

dp = Dispatcher()


def make_kb_for_start():
    kb = [
        [KeyboardButton(text="/Books")],
        [KeyboardButton(text="/Games")],
        [KeyboardButton(text="/Movies")],
        [KeyboardButton(text="/help")],
    ]

    keyboard = ReplyKeyboardMarkup(
        keyboard=kb, resize_keyboard=True,
        input_field_placeholder="what's your target"
    )
    return keyboard


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
    raise NotImplementedError()


@dp.message(Command("games", ignore_case=True))
async def games_handler(message: Message):
    """
    docs will be here
    """
    raise NotImplementedError()


@dp.message(Command("movies", ignore_case=True))
async def movies_handler(message: Message):
    """
    docs will be here
    """
    raise NotImplementedError()


async def main():
    bot = Bot(settings.BOT_TOKEN)

    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
