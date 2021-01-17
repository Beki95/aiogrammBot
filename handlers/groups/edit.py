import io

from aiogram import types
from aiogram.dispatcher.filters import Command

from filters.ADmin import AdminFilter
from loader import dp, bot

"""команда для установки фото на профиль группы"""


@dp.message_handler(Command("set_photo", prefixes="!/"), AdminFilter())
async def set_photo(message: types.Message):
    # переменная которая берет ответ
    sourse = message.reply_to_message
    # из переменной sourse вытаскиваем фото с самым высоким разрешением
    photo = sourse.photo[-1]
    # в переменныю фото загружаем временные данные в виде байтов
    photo = await photo.download(destination=io.BytesIO())
    input_file = types.InputFile(path_or_bytesio=photo)
    # await bot.set_chat_photo(chat_id=message.chat.id, photo=input_file)
    
    await message.chat.set_photo(input_file)


# Команда для установки описания группы
@dp.message_handler(Command("set_description", prefixes="!/"), AdminFilter())
async def set_description(message: types.Message):
    sourse = message.reply_to_message
    description = sourse.text
    await message.chat.set_description(description)


# Команда для установки название группы
@dp.message_handler(Command("set_title", prefixes="!/"), AdminFilter())
async def set_title(message: types.Message):
    sourse = message.reply_to_message
    title = sourse.text
    await message.chat.set_title(title)
