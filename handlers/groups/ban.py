import asyncio
import re
from datetime import datetime, timedelta

from aiogram import types
from aiogram.dispatcher.filters import Command

from filters.ADmin import AdminFilter
from loader import dp


@dp.message_handler(Command("ro", prefixes="!/"), AdminFilter())
async def command_ro(message: types.Message):
    member = message.reply_to_message.from_user
    member_id = member.id
    chat_id = message.chat.id
    command_parse = re.compile(r"(!ro|/ro) ?(\d+)? ?([\w+\D]+)?")
    parsed = command_parse.match(message.text)
    time = parsed.group(2)
    comment = parsed.group(3)

    if not time:
        time = 5
    else:
        time = int(time)
    until_date = datetime.now() + timedelta(minutes=time)

    ReadonlyPermissions = types.ChatPermissions(
        can_send_polls=False,
        can_change_info=False,
        can_pin_messages=False,
        can_invite_users=True,
        can_send_messages=False,
        can_add_web_page_previews=False,
        can_send_other_messages=False,
        can_send_media_messages=False
    )
    try:
        await message.chat.restrict(user_id=member_id, until_date=until_date, permissions=ReadonlyPermissions)
        await message.reply(f"Пользователю нельзя писать {time} минут по причине {comment}")
    except Exception as ex:
        print(ex)


@dp.message_handler(Command("unro", prefixes="!/"), AdminFilter())
async def command_ro(message: types.Message):
    member_ = message.reply_to_message.from_user
    member_id = member_.id
    chat_id = message.chat.id

    ReadonlyPermissions = types.ChatPermissions(
        can_send_polls=True,
        can_change_info=True,
        can_pin_messages=True,
        can_invite_users=True,
        can_send_messages=True,
        can_add_web_page_previews=True,
        can_send_other_messages=True,
        can_send_media_messages=True
    )
    try:
        await message.chat.restrict(user_id=member_id, until_date=0, permissions=ReadonlyPermissions)
        await message.reply(f"Пользовател был разбанен")
    except Exception as ex:
        print(ex)

    service_mess = await message.reply("сообщение удалится через 5 сек")
    await asyncio.sleep(5)
    await message.delete()
    await service_mess.delete()


@dp.message_handler(Command("ban", prefixes="!/"), AdminFilter())
async def command_ban(message: types.Message):
    member = message.reply_to_message.from_user
    member_id = member.id
    await message.chat.kick(user_id=member_id, until_date=0)
    await message.reply(f"Пользователь {member.full_name} был забанен")


@dp.message_handler(Command("unban", prefixes="!/"), AdminFilter())
async def command_ban(message: types.Message):
    member = message.reply_to_message.from_user
    member_id = member.id
    await message.chat.unban(user_id=member_id)
    await message.reply(f"Пользователь {member.full_name} был разбанен")


