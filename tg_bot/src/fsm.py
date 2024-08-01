from aiogram.fsm.state import State, StatesGroup


class BookEnterState(StatesGroup):
    enter_name = State()
    enter_status = State()
    enter_rate = State()
    enter_review = State()
    enter_genre = State()
    enter_author = State()


class GameEnterState(StatesGroup):
    enter_name = State()
    enter_status = State()
    enter_rate = State()
    enter_review = State()
    enter_genre = State()


class MovieEnterState(StatesGroup):
    enter_name = State()
    enter_status = State()
    enter_rate = State()
    enter_review = State()
    enter_genre = State()
    enter_director = State()


class CommonDeleteState(StatesGroup):
    enter_name = State()


class BookDeleteState(CommonDeleteState):
    pass


class GameDeleteState(CommonDeleteState):
    pass


class MovieDeleteState(CommonDeleteState):
    pass
