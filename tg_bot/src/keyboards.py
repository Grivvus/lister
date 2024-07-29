from aiogram.types import (
    ReplyKeyboardMarkup,
    KeyboardButton,
    InlineKeyboardButton
)
from aiogram.utils.keyboard import InlineKeyboardBuilder


def make_kb_for_start() -> ReplyKeyboardMarkup:
    """
    returns keyboard entity on '/start' command
    """
    kb = [
        [KeyboardButton(text="/Books")],
        [KeyboardButton(text="/Games")],
        [KeyboardButton(text="/Movies")],
        [KeyboardButton(text="/help")],
        [KeyboardButton(text="/clear")]
    ]

    keyboard = ReplyKeyboardMarkup(
        keyboard=kb, resize_keyboard=True,
        input_field_placeholder="what's your target"
    )
    return keyboard


def get_first_level_inline_keyboard(type: str) -> InlineKeyboardBuilder:
    """
    returns keyboard
    """
    builder = InlineKeyboardBuilder()
    builder.add(
        InlineKeyboardButton(text="Добавить", callback_data=f"add_{type}")
    )
    builder.add(
        InlineKeyboardButton(text="Изменить", callback_data=f"change_{type}")
    )
    builder.add(
        InlineKeyboardButton(text="Удалить", callback_data=f"del_{type}")
    )
    builder.add(
        InlineKeyboardButton(
            text="Весь список", callback_data=f"get_all_{type}"
        )
    )
    builder.add(
        InlineKeyboardButton(text="Взять сверху", callback_data=f"pop_{type}")
    )

    builder.adjust(3)

    return builder


def get_possible_statuses_keyboard() -> ReplyKeyboardMarkup:
    kb = [
        [KeyboardButton(text="not started")],
        [KeyboardButton(text="in progress")],
        [KeyboardButton(text="finished")],
    ]

    keyboard = ReplyKeyboardMarkup(
        keyboard=kb, resize_keyboard=True,
        input_field_placeholder="what's book status?"
    )

    return keyboard


def get_possible_rate() -> ReplyKeyboardMarkup:
    kb = [
        [KeyboardButton(text="0")],
        [KeyboardButton(text="1")],
        [KeyboardButton(text="2")],
        [KeyboardButton(text="3")],
        [KeyboardButton(text="4")],
        [KeyboardButton(text="5")],
        [KeyboardButton(text="6")],
        [KeyboardButton(text="7")],
        [KeyboardButton(text="8")],
        [KeyboardButton(text="9")],
        [KeyboardButton(text="10")]
    ]

    keyboard = ReplyKeyboardMarkup(
        keyboard=kb, resize_keyboad=True,
        input_field_placeholder="what's your rate of this book"
    )

    return keyboard
