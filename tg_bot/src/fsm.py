from aiogram.fsm.state import State
from aiogram.fsm.state import StatesGroup


class BookEnterState(StatesGroup):
    enter_name = State()
    enter_author = State()
    enter_genre = State()
    enter_status = State()
    enter_rate = State()
    enter_review = State()
    is_ready = State()


class BookDeleteState(StatesGroup):
    enter_name = State()
