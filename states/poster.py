
# StatesGroup State
from aiogram.dispatcher.filters.state import StatesGroup, State


class New_post(StatesGroup):
    EnterMessage = State()
    Confirm = State()