import json

import telebot
from telebot import types
from telebot.callback_data import CallbackData
import requests

import settings

BASE_URL = "http://127.0.0.1:8000"
HELP_TEXT = ""
bot = telebot.TeleBot(token=settings.TOKEN)

@bot.message_handler(commands=["start"])
def start(message: types.Message):
    print(message.chat)
    bot.send_message(message.chat.id, "Hello there")
    bot.send_message(message.chat.id, HELP_TEXT)

@bot.message_handler(commands=["help", "commands"])
def help(message: types.Message):
    bot.send_message(message.chat.id, HELP_TEXT)
@bot.message_handler(commands=["add_book"])
def add_book(message: types.Message):
    data: list[str] = message.text.split()


@bot.message_handler(commands=["add_game"])
def add_game(message: types.Message):
    data: list[str] = message.text.split()


@bot.message_handler(commands=["add_movie"])
def add_movie(message: types.Message):
    data_raw: list[str] = message.text.split()
    data: dict = {}
    try:
        data["title"] = data_raw[1]
        try:
            data["link"] = data_raw[2]
        except IndexError:
            pass
    except Exception as e:
        print(e)
        bot.send_message(message.chat.id, f"Ошибка при добавлении фильма {e}")
    print(data)
    r = requests.post(f"{BASE_URL}/add_movie/{message.chat.id}", data=json.dumps(data))
    if r.status_code == 200:
        bot.send_message(message.chat.id,
                         f"Movie {data['title']} succesfully added"
        )
    else:
        bot.send_message(message.chat.id,
                         "Unexpected error, request return"\
                         + f"status {r.status_code}"
        )


# @bot.message_handler(commands=["add"])
# def add_item(message: types.Message):
#     bot.send_message(
#         message.chat.id,
#         text= "Which type of content do you want to add",
#         reply_markup=bot_utils.generate_buttons_markup()
#     )


# не работающая шляпа
# @bot.callback_query_handler(func=lambda param: True)
# def callback_query(call: types.CallbackQuery):
#     if call.data == "book":
#         bot.send_message(call.from_user.id, "add book to db")
#     elif call.data == "movie":
#         bot.send_message(call.from_user.id, "add movie to db")
#     elif call.data == "game":
#         bot.send_message(call.from_user.id, "add game to db")


bot.infinity_polling()
