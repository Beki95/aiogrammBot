import asyncio

from utils.db_api.postgres import Database


async def test():

    print("созадаем таблицу для user")
    print(await db.create_table_users())

    # print("созадаем таблицу для kino")
    # print(await db.create_table_kino(name_table="kinos"))

    # print(await db.delete_user(1))

    # print(await db.count_user())
    # print(await db.select_kino("kinos", "та"))


loop = asyncio.get_event_loop()
db = Database(loop)
loop.run_until_complete(test())
