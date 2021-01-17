import asyncio
from datetime import datetime
import datetime as date

import schedule as schedule
from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command

from loader import dp
import time
from states.test import DATESs


@dp.message_handler(Command("datecom"))
async def get_text(message: types.Message):
    await message.answer("бот будет тебе отправлять сообщение каждые 10 сек\n\n"
                         "если хочешь запустить нажми 1 иначе break")
    await DATESs.q.set()


@dp.message_handler(state=DATESs.q)
async def get_(message: types.Message, state: FSMContext):
    wait = 5
    await DATESs.q2.set()
    while True:
        if message.text == "break":
            await message.answer("ok")
            break
        else:
            await asyncio.sleep(wait)
            now = datetime.utcnow()
            await message.answer(f"{now}", disable_notification=True)
    await state.finish()


