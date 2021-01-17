from typing import Union

from aiogram import Bot


async def subscription(user_id, channel_id: Union[int, str]):
    bot = Bot.get_current()
    member = await bot.get_chat_member(user_id=user_id, chat_id=channel_id)
    print(member)
    return member.is_chat_member()
