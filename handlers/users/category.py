from aiogram import types
from aiogram.dispatcher.filters import Command

from keyboards.default.board import menu
from keyboards.inline.inline_button import category_inline
from keyboards.inline.serialy_button import serialyButton
from loader import dp


@dp.message_handler(content_types=types.ContentType.TEXT)
async def get_category(message: types.Message):
    if message.text == "🗂Категории":
        await message.answer(text="🗂Категории", reply_markup=category_inline)
    elif message.text == "🕞time post":
        await message.answer(text=f"{message.text}")
    elif message.text == "📰Последнее":
        await message.answer(text=f"{message.text}")
    elif message.text == "🏮Аниме":
        await message.answer(text=f"{message.text}")
    elif message.text == "🎬Рандомный трейлер":
        await message.answer(text=f"{message.text}")
    elif message.text == "🛋Сериалы":
        await message.answer(text=f"{message.text}", reply_markup=serialyButton)