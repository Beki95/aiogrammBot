import asyncio

import asyncpg

from data import config


class Database:

    def __init__(self, loop: asyncio.AbstractEventLoop):
        self.pool: asyncio.pool.Pool = loop.run_until_complete(
            asyncpg.create_pool(
                user=config.PGUSER,
                password=config.PGPASSWORD,
                host=config.ip
            )
        )

    async def create_table_users(self):
        sql = """
            CREATE TABLE IF NOT EXISTS users(id INTEGER NOT NULL,
             name VARCHAR(255) NOT NULL,
             status INTEGER NOT NULL,
              PRIMARY KEY (id));
            """
        await self.pool.execute(sql)

    async def create_table_kino(self, name_table):
        sql = f"""
            CREATE table IF NOT EXISTS {name_table}(id INTEGER, name TEXT, link TEXT, photo TEXT, PRIMARY KEY (id));
            """
        await self.pool.execute(sql)

    async def delete_user(self, user_id):
        sql = f"""
            DELETE FROM users WHERE id = {user_id};
            """
        await self.pool.execute(sql)

    async def create_user(self, id, name, status):
        sql = f"""
            INSERT INTO users Values ({id}, '{name}', {status})
            """
        await self.pool.execute(sql)

    async def delete_table(self, name_table):
        sql = f"""
            DROP TABLE {name_table};
            """
        await self.pool.execute(sql)

    # Доделать !!!!!!!!!!!

    async def select_kino(self, table, kino):
        sql = f"""
            SELECT name, link, photo FROM {table} WHERE name LIKE '%{kino}%' LIMIT 7
            """
        return await self.pool.fetch(sql)

    async def count_user(self):
        sql = """
            SELECT count(*) FROM user;
            """

        return await self.pool.fetchval(sql)

    async def insert_into(self, id, name, link, photo, table):
        sql = f"""
            INSERT INTO {table} Values ({id}, '{name}', '{link}', '{photo}')
            """
        await self.pool.execute(sql)
# Database(loop=asyncio.get_event_loop())
