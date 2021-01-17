from aiogram import types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, message
from aiogram.utils.callback_data import CallbackData

check_button = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Проверить подписку", callback_data="check")
        ]
    ]
)

post_callback = CallbackData("create_post", "action")

confermation_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Опубликовать пост", callback_data=post_callback.new(action="post")),
            InlineKeyboardButton(text="Отклонить пост", callback_data=post_callback.new(action="cancel")),
        ]
    ]
)

code_addres = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Узнать", callback_data="code")
        ]
    ]
)