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
            CREATE TABLE IF NOT EXISTS Users(
            id int not null, 
            name text not null, 
            email text,
            Primary Key (id)
            );
            """
        await self.pool.execute(sql)

    @staticmethod
    def format_args(sql, parameters: dict):
        sql += " AND ".join([
            f"{item} = ${num}" for num, item in enumerate(parameters, start=1)
        ])
        return sql, tuple(parameters.values())

    async def create_user(self, id: int, name: str, email: str = None):
        sql = """
            INSERT INTO Users (id, name, email)  
            VALUES ($1, $2, $3)
        """
        await self.pool.execute(sql, id, name, email)

    async def select_all_users(self):
        sql = """
            SELECT * FROM Users
        """
        return await self.pool.fetch(sql)

    async def select_user(self, **kwargs):
        sql = """SELECT * FROM Users WHERE """
        sql, parameters = self.format_args(sql, kwargs)
        return await self.pool.fetchrow(sql, *parameters)

    async def count_users(self):
        sql = """
            SELECT count(*) FROM Users
        """
        return await self.pool.fetchval(sql)

    async def update_email(self, email, id):
        sql = """
            UPDATE Users SET email=$1 WHERE id=$2
        """
        await self.pool.execute(sql, email, id)

    async def delete_users(self):
        sql = """
            DELETE FROM Users WHERE TRUE
        """
        await self.pool.execute(sql)



