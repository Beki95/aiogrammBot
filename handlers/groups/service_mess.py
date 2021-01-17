from aiogram import types

from loader import dp, bot


@dp.message_handler(content_types=types.ContentType.NEW_CHAT_MEMBERS)
async def edit_new_member(message: types.Message):
    new_member = ", ".join([m.get_mention(as_html=True) for m in message.new_chat_members])
    await message.reply(f"Привет {new_member}.")


@dp.message_handler(content_types=types.ContentType.LEFT_CHAT_MEMBER)
async def left_member(message: types.Message):
    if message.left_chat_member.id == message.from_user.id:
        await message.answer(f"{message.left_chat_member.get_mention(as_html=True)} покинул группу")
    elif message.left_chat_member.id == (await bot.me).id:
        return
    else:
        await message.answer(f"{message.left_chat_member.full_name} был удален из чата {message.from_user.full_name}")
