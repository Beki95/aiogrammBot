import asyncio
from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart, Command

from keyboards.default.board import menu
from loader import dp
from utils.db_api.postgres import Database

"""Команды старт для запуска бота"""

loop = asyncio.get_event_loop()
db = Database(loop)


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    await message.answer(f"Привет {message.from_user.full_name}/n"
                         f"Добрый день, Этот бот поможет тебе найти фильм по твоему вкусу")
    await message.answer("🔍Чтобы найти фильм просто напишите его название", reply_markup=menu)
    id = message.from_user.id
    name = message.from_user.username
    await db.create_user(id=id, name=name, status=0)
