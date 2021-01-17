from aiogram import types
from aiogram.dispatcher.filters import CommandStart
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from data.config import allowed_users
from loader import dp


@dp.inline_handler(text="")
async def emty_query(query: types.InlineQuery):
    await query.answer(
        results=[
            types.InlineQueryResultArticle(
                id="unknown",
                title="Введите какой-то запрос",
                input_message_content=types.InputTextMessageContent(
                    message_text="Ну необязательно нажимать на кнопку"
                )
            )
        ],
        cache_time=5
    )


@dp.inline_handler()
async def some_query(query: types.InlineQuery):
    user = query.from_user.id
    if user not in allowed_users:
        print(True)
        await query.answer(
            results=[],
            switch_pm_text="Бот недоступен подключиться к боту",
            switch_pm_parameter="connect_user",
            cache_time=5
        )
        return

    await query.answer(
        results=[
            types.InlineQueryResultArticle(
                id="2",
                title="Название которое отображается в инлайн режиме",
                input_message_content=types.InputTextMessageContent(
                    message_text="Тут будет выведен какой-то текст который будет отправлен при нажатии на кнопку",
                ),
                url="https://core.telegram.org/bots/api#inputmessagecontent",
                thumb_url="https://i.pinimg.com/736x/f7/d2/8c/f7d28c21daeafab7bc59682fd944bf40.jpg",
                description="какое-то описание в инлайн режиме"
            ),
            types.InlineQueryResultVideo(
                id="4",
                video_url="https://vod.wix.com/public/download/0a01b8b1ce0f47a090f3b77e1b496290/redirect?instance=HPBVQBVXSfVLXzmO_lRmN2iSFd-6xSpML32LNDIPLNc.eyJpbnN0YW5jZUlkIjoiNDY0MzI5ZWYtY2IxYS00NTQyLWFmYWUtMjY5ZmJjYmU2ZjE3IiwiYXBwRGVmSWQiOiIxNDQwOTU5NS1mMDc2LTQ3NTMtODMwMy05YTg2ZjlmNzE0NjkiLCJtZXRhU2l0ZUlkIjoiYWQwYzA2MGEtODAzMC00YWMxLThmMDAtNjMyYTM4ODg5MTY2Iiwic2lnbkRhdGUiOiIyMDIwLTEyLTI1VDE5OjAyOjI3Ljg4NFoiLCJ2ZW5kb3JQcm9kdWN0SWQiOiJDb25uZWN0IERvbWFpbiArIFdpeCBWaWRlbyIsImRlbW9Nb2RlIjpmYWxzZSwiYWlkIjoiYWZmNWNkMzctNjVmZC00YmFmLTg5YWMtNzQ1ZTRmMTFlMWMwIiwiYmlUb2tlbiI6ImViNGYyZmU1LTRiMmEtMGY4My0yMGFlLTQ1YjU4NDM2ZmU3MSIsInNpdGVPd25lcklkIjoiNjMyZDYxZTgtZmVhZC00ZTQyLTkxYzctMzUzODQxYTA1YzZkIn0&channel_id=a339329101d04f069901cdb109d244ed",
                caption="Подпись к видео",
                title="какое-то видео",
                thumb_url="http://pm1.narvii.com/7078/b2b2aaf6f18400286928ff28e2fb180038e93800r1-811-1075v2_uhq.jpg",
                mime_type="video/mp4"
            )
        ],
        cache_time=5
    )


@dp.message_handler(CommandStart(deep_link="connect_user"))
async def connect_user(message: types.Message):
    allowed_users.append(message.from_user.id)
    await message.answer("Вы подключены", reply_markup=InlineKeyboardMarkup(
        inline_keyboard=[[
            InlineKeyboardButton(
                text="Войти в инлайн режим",
                switch_inline_query_current_chat="Запрос"
            )]
        ]
    ))
