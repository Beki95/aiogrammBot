from aiogram.dispatcher.filters.state import StatesGroup, State


class Poisk(StatesGroup):
    search = State()
    search2 = State()
