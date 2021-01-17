import asyncio

from utils.db_api.postgresql import Database


async def test():
    await db.delete_users()
    print("Создаем таблицу пользователя")
    await db.create_table_users()
    print("Таблица создана")
    print("Добовляем пользователей")
    await db.create_user(1, "beki", "beki@gmail.com")
    await db.create_user(2, "Two", "2@gmail.com")
    await db.create_user(3, "three", "3@gmail.com")
    await db.create_user(4, "ьыо", "dssd")
    await db.create_user(5, "sd", "55")
    print("Готово")

    users = await db.select_all_users()
    print(f"Получаем всех пользователей {users}")

    user = await db.select_user(id=1, name="beki")
    print(f"Получаем пользователя {user}")

    count = await db.count_users()
    print(f"Пользователей в базе {count}")


loop = asyncio.get_event_loop()
db = Database(loop)
loop.run_until_complete(test())
