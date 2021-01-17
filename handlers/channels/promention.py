from aiogram import types
from aiogram.dispatcher.filters import Command

from data.config import chanels
from filters.is_forward import IsForward
from keyboards.inline.check import check_button
from loader import dp, bot
from utils.misc.subscription import subscription


@dp.message_handler(IsForward(), content_types=types.ContentTypes.ANY)
async def is_forward(message: types.Message):
    await message.answer(f'Сообщение было прислано из канала {message.forward_from_chat.title}.\n'
                         f'User_name: @{message.forward_from_chat.username}\n'
                         f'ID: {message.forward_from_chat.id}')


@dp.message_handler(Command("channels", prefixes="!/"))
async def command_forward(message: types.Message):
    chanels_format = str()
    for chanel_id in chanels:
        chat = await bot.get_chat(chat_id=chanel_id)
        invite_link = await chat.export_invite_link()  # можно еще через bot.export_invite_link(chat_id)
        chanels_format += f"Канал <a href='{invite_link}'>{chat.title}</a>"
    await message.answer(f"Вам необходимо подписаться на эти каналы:\n\n"
                         f"{chanels_format}",
                         reply_markup=check_button)


@dp.callback_query_handler(text="check")
async def check_button_(call: types.CallbackQuery):
    await call.answer()
    results = str()
    for chanel in chanels:
        status = await subscription(user_id=call.from_user.id, channel_id=chanel)
        chanel = await bot.get_chat(chanel)
        invite_link = await chanel.export_invite_link()
        if status:
            results += f"Подписка на Канал <b>{chanel.title}</b> Оформлена\n\n"
        else:
            results += (f"Подписка на канал <b>{chanel.title}</b> не оформлена "
                        f"<a href='{invite_link}'>'Нужно подписаться'</a>\n\n")
    await call.message.answer(results)
