import asyncio
from aiogram import types
from aiogram.dispatcher.filters import Command

from loader import dp
from utils.db_api.postgres import Database

loop = asyncio.get_event_loop()
db = Database(loop)


@dp.message_handler(Command("sub"))
async def subscribe(message: types.Message):
    await message.answer("Спасибо за Подписку 🙃")
    id = message.from_user.id
    name = message.from_user.username
    await db.create_user(id=id, name=name, status=1)