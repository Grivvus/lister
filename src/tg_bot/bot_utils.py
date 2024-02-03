from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

def generate_buttons_markup():
    markup = InlineKeyboardMarkup()
    markup.row_width = 3
    markup.add(
        InlineKeyboardButton("Book",
                             callback_data="book"),
        InlineKeyboardButton(
            "Movie", callback_data="movie"
        ),
        InlineKeyboardButton(
            "Game", callback_data="game"
        ),
    )

    return markup