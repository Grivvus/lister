from aiogram.fsm.state import State
from aiogram.fsm.state import StatesGroup


class BookEnterState(StatesGroup):
    start_state = State()
    enter_book_name = State()
    enter_book_author = State()
    enter_book_genre = State()
    enter_book_status = State()
    enter_book_rate = State()
    enter_book_review = State()
    is_ready = State()
