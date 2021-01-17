from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command
from google_trans_new import google_translator

from loader import dp
from states.test import DATE


@dp.message_handler(Command("translate"))
async def translate(message: types.Message, state: FSMContext):
    await message.answer("Пришли мне текст который надо перевести")
    await DATE.s.set()


@dp.message_handler(state=DATE.s)
async def translate_(message: types.Message, state: FSMContext):
    tr = google_translator()
    text = message.text
    results = tr.translate(text, lang_tgt="en")
    try:
        await message.answer(f"{results}")
    except:
        pass
