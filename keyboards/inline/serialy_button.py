from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

serialyButton = InlineKeyboardMarkup(row_width=2,
                                     inline_keyboard=[
                                         [
                                             InlineKeyboardButton("Русские", callback_data="button_1"),
                                             InlineKeyboardButton("ТНТ", callback_data="button_2"),
                                         ], [
                                             InlineKeyboardButton("СТС", callback_data="button_3"),
                                             InlineKeyboardButton("НТВ", callback_data="button_4"),
                                         ], [

                                             InlineKeyboardButton("Зарубежные", callback_data="button_5"),
                                             InlineKeyboardButton("Netflix", callback_data="button_6"),
                                         ], [
                                             InlineKeyboardButton("Дорамы", callback_data="button_7"),
                                             InlineKeyboardButton("Все", callback_data="button_8"),
                                         ]
                                     ]
                                     )
