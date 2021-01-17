from aiogram.dispatcher.filters.state import StatesGroup, State


class Test(StatesGroup):
    Q1 = State()
    Q2 = State()


class Email(StatesGroup):
    step = State()
    step2 = State()


class DATESs(StatesGroup):
    q = State()
    q2 = State()

class DATE(StatesGroup):
    s = State()
    s1 = State
