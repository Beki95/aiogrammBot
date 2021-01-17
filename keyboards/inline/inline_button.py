from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from keyboards.inline.callback_data import buy_callback


"""1 пример записи кнопок"""
choice = InlineKeyboardMarkup(row_width=2,
                              inline_keyboard=[
                                  [
                                      InlineKeyboardButton(
                                          text="ЯБЛОКИ", callback_data=buy_callback.new(item_text="apple", quantity=5)
                                      ),
                                      InlineKeyboardButton(
                                          text="Груши", callback_data="buy:pear:1"
                                      )
                                  ], [
                                      InlineKeyboardButton(
                                          text="отмена", callback_data="cancel"
                                      )
                                  ]
                              ]
                              )

"""2 пример записи кнопок"""
buy_link = InlineKeyboardMarkup()

LINK = "https://cloud.mail.ru/public/3SZk/eLPJ5TcJ3/%5BSuperSliv.biz%5D%204.2%20Инлайн%20Кнопки.mp4"

link = InlineKeyboardButton(text="купи тут", url=LINK)

buy_link.insert(link)
