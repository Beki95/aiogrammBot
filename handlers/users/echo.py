from aiogram import types
from loader import dp

@dp.message_handler()
async def bot_echo(message: types.Message):
    # Получаем chat_id и text
    chat_id = message.from_user.id
    text = message.text

    # Получим обьект бота Вариант 1 из диспатчера
    # bot = db.bot

    # Получим обьект бота Вариант 2 из контекста
    # from aiogram import Bot
    # bot = Bot.get_current()

    # Получим обьект бота Вариант 3 из модуля loader
    from loader import bot

    # отправим ответ пользователю Вариант 1
    await bot.send_message(chat_id=chat_id, text=text)

    # Вариант 2 без chat_id
    # await message.answer(text)

    # Вариант 3 с реплаем
    # await message.reply(text=text)
