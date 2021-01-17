from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

menu = ReplyKeyboardMarkup(
    [
        [
            KeyboardButton(text="Котлетки")
        ],
        [
            KeyboardButton("Макарошки"),
            KeyboardButton("Пюрешки"),
        ]
    ],
    resize_keyboard=True
)