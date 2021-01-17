from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

location = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="🔎", request_location=True)
        ]
    ],
    resize_keyboard=True
)
contact = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="📞", request_contact=True)
        ]
    ],
    resize_keyboard=True
)