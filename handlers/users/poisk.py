import asyncio
from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command
from aiogram.types import MediaGroup

from loader import dp, bot
from states.STATES import Poisk
from utils.db_api.postgres import Database

loop = asyncio.get_event_loop()
db = Database(loop)


@dp.message_handler(content_types=types.ContentType.TEXT)
async def state_search(message: types.Message):
    albom = MediaGroup()
    text = ""
    name = str(message.text.lower())
    name_kino = await db.select_kino("kinos", name)
    if not name_kino:
        await message.answer("Такого названия нет либо остановите поиск\n/stop")
    for i in name_kino:
        text += f"<a href='{i[1]}'>{i[0]}</a>\n"
        albom.attach_photo(f"{i[2]}", caption=f"{i[0]} - {i[1]}")
    await message.answer_media_group(media=albom)
    await bot.send_message(chat_id=message.chat.id, text=text, parse_mode="HTML", disable_web_page_preview=True)