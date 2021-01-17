from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart, Command

from loader import dp

"""Команды старт для запуска бота"""


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    await message.answer(f"Привет {message.from_user.full_name}")