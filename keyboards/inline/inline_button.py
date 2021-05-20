from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

category_inline = InlineKeyboardMarkup(row_width=2,
                                       inline_keyboard=[
                                           [
                                               InlineKeyboardButton(text="Биография", callback_data="buttonk1"),
                                               InlineKeyboardButton(text="Боевики", callback_data="buttonk2"),
                                           ], [
                                               InlineKeyboardButton(text="Вестерны", callback_data="buttonk3"),
                                               InlineKeyboardButton(text="Военные", callback_data="buttonk4"),
                                           ], [
                                               InlineKeyboardButton(text="Детективы", callback_data="buttonk5"),
                                               InlineKeyboardButton(text="Драма", callback_data="buttonk7"),
                                           ], [
                                               InlineKeyboardButton(text="Исторические", callback_data="buttonk8"),
                                               InlineKeyboardButton(text="Комедии", callback_data="buttonk9"),
                                           ], [
                                               InlineKeyboardButton(text="Криминал", callback_data="buttonk10"),
                                               InlineKeyboardButton(text="Фантастика", callback_data="buttonk19"),
                                           ], [
                                               InlineKeyboardButton(text="Мультфильмы", callback_data="buttonk12"),
                                               InlineKeyboardButton(text="Мюзиклы", callback_data="buttonk13"),
                                           ], [
                                               InlineKeyboardButton(text="Приключения", callback_data="buttonk14"),
                                               InlineKeyboardButton(text="Семейные", callback_data="buttonk15"),
                                           ], [
                                               InlineKeyboardButton(text="Спортивные", callback_data="buttonk16"),
                                               InlineKeyboardButton(text="Триллеры", callback_data="buttonk17"),
                                           ], [
                                               InlineKeyboardButton(text="Ужасы", callback_data="buttonk18"),
                                               InlineKeyboardButton(text="Фэнтези", callback_data="buttonk20")
                                           ]
                                       ]
                                       )
