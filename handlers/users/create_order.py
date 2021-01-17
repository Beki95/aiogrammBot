from aiogram import types
from aiogram.dispatcher.filters import Command

from data.item import Tesla_model_S, PICUP, POST_FAST_SHIPPING, POST_REGULAR_SHIPPING
from loader import dp, bot


@dp.message_handler(Command("invoices"))
async def command_invoices(message: types.Message):
    await bot.send_invoice(message.from_user.id,
                           **Tesla_model_S.generate_invoice()
                           )


@dp.shipping_query_handler()
async def shipping_query(query: types.ShippingQuery):
    if query.shipping_address.country_code == "KG":
        await bot.answer_shipping_query(shipping_query_id=query.id,
                                        ok=True,
                                        shipping_options=[POST_REGULAR_SHIPPING, POST_FAST_SHIPPING, PICUP])
    elif query.shipping_address.country_code == "RU":
        await bot.answer_shipping_query(shipping_query_id=query.id,
                                        ok=True,
                                        shipping_options=[POST_REGULAR_SHIPPING])
    elif query.shipping_address.country_code == "UA":
        await bot.answer_shipping_query(shipping_query_id=query.id,
                                        ok=True,
                                        shipping_options=[POST_FAST_SHIPPING])
    else:
        await bot.answer_shipping_query(shipping_query_id=query.id,
                                        ok=False,
                                        error_message="Суда недостовляем")


@dp.pre_checkout_query_handler()
async def pre_checkout_query(query: types.PreCheckoutQuery):
    await bot.answer_pre_checkout_query(pre_checkout_query_id=query.id,
                                        ok=True)
    await bot.send_message(query.from_user.id, text="Оплата прошла успешно")
