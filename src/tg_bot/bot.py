import json

import telebot
from telebot import types
from telebot.callback_data import CallbackData
import requests

from bot_utils import BASE_URL, check_for_permition
import settings

HELP_TEXT = "This bot called upon to structure your list of games, you want \
to play, books, you want to read, movies, you want to watch. \
There are some commands to interact with bot. \n\n\
/start - command to start communication with bot, \n\
/help - command that sending this text, \n\
/get_all_games(get_all_books, get_all_movies) - \
command that sending your list of games(books, movies) in priority order, \n\
/add_game(add_book, add_movie) - command to add game(book, movie) to your \
list, \n/pop_game(pop_book, pop_movie) - command that returns upper element\
and change it status at 'in progress' - means that you start to play this \
game(read book,etc...)"

bot = telebot.TeleBot(token=settings.TOKEN)

@bot.message_handler(commands=["start"])
def start(message: types.Message):
    bot.send_message(message.chat.id, "Hello there")
    bot.send_message(message.chat.id, HELP_TEXT)

@bot.message_handler(commands=["help", "commands"])
def help(message: types.Message):
    bot.send_message(message.chat.id, HELP_TEXT)


@bot.message_handler(commands=["get_all_games"])
def get_all_games(message: types.Message):
    r = requests.get(url=f"{BASE_URL}/get_games_list/{message.chat.id}")
    if r.status_code == 200:
        s = ""
        resp = r.json()
        for i in resp:
            s += f"{resp[i]['title']} {resp[i]['link']} " +\
                f"{resp[i]['priority']} {resp[i]['status']} \n"
        bot.send_message(message.chat.id, s)
    else:
        bot.send_message(message.chat.id,
                         "Unexpected error, request return"\
                         + f"status {r.status_code}"
        )

@bot.message_handler(commands=["get_all_movies"])
def get_all_movies(message: types.Message):
    r = requests.get(url=f"{BASE_URL}/get_movies_list/{message.chat.id}")
    if r.status_code == 200:
        s = ""
        resp = r.json()
        for i in resp:
            s += f"{resp[i]['title']} {resp[i]['link']} " +\
                f"{resp[i]['priority']} {resp[i]['status']} \n"
        bot.send_message(message.chat.id, s)
    else:
        bot.send_message(message.chat.id,
                         "Unexpected error, request return"\
                         + f"status {r.status_code}"
        )

@bot.message_handler(commands=["get_all_books"])
def get_all_books(message: types.Message):
    r = requests.get(url=f"{BASE_URL}/get_books_list/{message.chat.id}")
    if r.status_code == 200:
        s = ""
        resp = r.json()
        for i in resp:
            s += f"{resp[i]['author']} {resp[i]['title']} {resp[i]['link']} "+\
                f"{resp[i]['priority']} {resp[i]['status']} \n"
        bot.send_message(message.chat.id, s)
    else:
        bot.send_message(message.chat.id,
                         "Unexpected error, request return"\
                         + f"status {r.status_code}"
        )


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


@bot.message_handler(commands=["pop_game"])
def pop_game(message: types.Message):
    r = requests.get(url=f"{BASE_URL}/pop_game/{message.chat.id}")
    if r.status_code == 200:
        resp = r.json()
        bot.send_message(f"you took game {resp['title']} to play")
    else:
        bot.send_message(message.chat.id,
                         "Unexpected error, request return"\
                         + f"status {r.status_code}"
        )

@bot.message_handler(commands=["pop_book"])
def pop_book(message: types.Message):
    r = requests.get(url=f"{BASE_URL}/pop_book/{message.chat.id}")
    if r.status_code == 200:
        resp = r.json()
        bot.send_message(f"you took book {resp['title']} to read")
    else:
        bot.send_message(message.chat.id,
                         "Unexpected error, request return"\
                         + f"status {r.status_code}"
        )

@bot.message_handler(commands=["pop_movie"])
def pop_movie(message: types.Message):
    r = requests.get(url=f"{BASE_URL}/pop_movie/{message.chat.id}")
    if r.status_code == 200:
        resp = r.json()
        bot.send_message(f"you took movie {resp['title']} to watch")
    else:
        bot.send_message(message.chat.id,
                         "Unexpected error, request return"\
                         + f"status {r.status_code}"
        )


bot.infinity_polling()
