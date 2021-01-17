import asyncio
from sqlite3 import IntegrityError

from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.builtin import CommandStart, Command

from loader import dp
from states.test import Email
from utils.db_api.postgresql import Database
db = Database(loop=asyncio.get_event_loop())


"""Команды старт для запуска бота"""


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    await message.answer(f'Привет, {message.from_user.full_name}!')
    id = message.from_user.id
    name = message.from_user.full_name
    user = await db.select_user(name=name, id=id)
    select_user = await db.select_all_users()
    tuples = [*select_user]
    t_users = []
    for i in tuples:
        t_users.append(i["id"])
    print(t_users)
    if id in t_users:
        await message.answer(f"Вы уже были добавлены в базу\n"
                             f"Если хотите можете добавить свой email: \n"
                             f"По этой команде /email,"
                             f"\nПо команде /user можете просмотреть свои данные в бд"
                             )
    elif id not in t_users:
        try:
            await db.create_user(id, name)
            await message.answer(f"Вы добавлены в базу "
                                 f"ваш имя {name} "
                                 f"Если хотите можете добавить свой email: \n"
                                 f"по команде /email")

        except IntegrityError:
            pass


@dp.message_handler(Command("user"))
async def select_user_(message: types.Message):
    name = message.from_user.full_name
    id = message.from_user.id
    s_u = await db.select_user(name=name, id=id)
    user_ = await db.select_all_users()
    await message.answer("Ваши данные такие \n<code>{id}, {name}, {email}</code>\n".format(**s_u))


@dp.message_handler(Command("email"))
async def email(message: types.Message):
    await message.answer("Пришли мне свой email")
    await Email.step.set()


@dp.message_handler(state=Email.step)
async def step(message: types.Message, state: FSMContext):
    n = ["gmail.com", "mail.ru"]
    email = message.text
    id = message.from_user.id
    check = None
    for i in n:
        if i in email:
            check = 1
    if check:
        await message.answer(f"Ваш email {email} был добавлен в базу")
        await db.update_email(email, id)
        s = await db.select_all_users()
        print(s)
        await state.finish()
    else:
        await message.answer(f"Вы неправильно ввели Email попробуйте еще раз")

