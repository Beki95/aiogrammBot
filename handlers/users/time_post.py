import asyncio
import datetime

from aiogram import types
from aiogram.dispatcher.filters import Command

from loader import dp


@dp.message_handler(Command('post'), content_types=types.ContentType.TEXT)
async def post_time(message: types.Message):
    await message.answer('бот будет тебе отправлять сообщение каждые 10 сек\n\n'
                         'если хочешь запустить нажми 1 иначе break')
    while True:
        await asyncio.sleep(3)
        now = datetime.datetime.now()
        await message.answer(f'{now}')
