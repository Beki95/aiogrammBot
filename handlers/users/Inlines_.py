from aiogram import types
from aiogram.dispatcher.filters import Command

from keyboards.inline.callback_data import buy_callback
from keyboards.inline.inline_button import choice, buy_link
from loader import dp

"""                             Это handler для инлайн кнопок                              """


@dp.message_handler(Command("inlines"))
async def show_inlines(message: types.Message):
    await message.answer("Хочешь купить что то так выбери: Яблоки в количестве 5 шт, Груши в количестве 1",
                         reply_markup=choice)


@dp.callback_query_handler(buy_callback.filter(item_text="apple"))
async def apple(call: types.CallbackQuery, callback_data: dict):
    await call.answer(cache_time=60)
    quantity = callback_data.get("quantity")
    await call.message.answer(f"Вы выбрыли купить Яблоки. Яблок всего {quantity}. Спасибо",
                              reply_markup=buy_link)


@dp.callback_query_handler(buy_callback.filter(item_text="pear"))
async def apple(call: types.CallbackQuery, callback_data: dict):
    await call.answer(cache_time=60)
    quantity = callback_data.get("quantity")
    await call.message.answer(f"Вы выбрыли купить Грушу. Груш всего {quantity}. Спасибо",
                              reply_markup=buy_link)


@dp.callback_query_handler(text="cancel")
async def apple(call: types.CallbackQuery):
    await call.answer("Вы отменили покупку", show_alert=True)
    await call.message.edit_reply_markup()
