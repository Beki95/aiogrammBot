from aiogram import types
from aiogram.dispatcher.filters import BoundFilter


class IsForward(BoundFilter):
    async def check(self, message: types.Message) -> bool:
        if message.forward_from_chat:
            return message.forward_from_chat.type == types.ChatType.CHANNEL