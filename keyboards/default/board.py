from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="🗂Категории"),
            KeyboardButton(text="📰Последнее"),
            KeyboardButton(text="🛋Сериалы")
        ],
        [
            KeyboardButton(text="📺TV"),
            KeyboardButton(text="🏮Аниме"),
            KeyboardButton(text="🕞time post")
        ],
        [
            KeyboardButton(text="🎈Мультсериалы"),
            KeyboardButton(text="🎬Рандомный трейлер"),
            KeyboardButton(text="🧸Мульт")
        ]
    ],
    resize_keyboard=True
)
