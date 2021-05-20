from aiogram import types
from handlers.users import sub


async def set_defalt_command(dp):
    await dp.bot.set_my_commands([
        types.BotCommand("start", "Запуск бота"),
        types.BotCommand("help", "Помощь"),
    ])