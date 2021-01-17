import sqlite3


class Database:

    def __init__(self, path_to_db="utils/db_api/main.db"):
        self.path_to_db = path_to_db

    @property
    def connection(self):
        return sqlite3.connect(self.path_to_db)

    def execute(self, sql, parametrs: tuple = None, fetchone=False,
                fetchall=False, commit=False):
        if not parametrs:
            parametrs = tuple()
        connection = self.connection
        connection.set_trace_callback(logger)
        cursor = connection.cursor()
        cursor.execute(sql, parametrs)
        data = None

        if fetchone:
            data = cursor.fetchone()
        if fetchall:
            data = cursor.fetchall()
        if commit:
            connection.commit()
        connection.close()

        return data

    def create_table_users(self):
        sql = """CREATE TABLE IF NOT EXISTS Users(
        id int NOT NULL, name varchar(255) NOT NULL,
        email varchar(255),
        Primary Key (id)
        )"""
        self.execute(sql, commit=True)

    def add_user(self, id: int, name: str, email: str = None):
        sql = """INSERT INTO Users (id, name, email) VALUES 
        (?, ?, ?);
        """
        parametrs = (id, name, email)
        return self.execute(sql, parametrs=parametrs, commit=True)

    def select_all_users(self):
        sql = """SELECT * FROM Users"""
        return self.execute(sql, fetchall=True)

    @staticmethod
    def format_args(sql, parametrs: dict):
        sql += " AND ".join([
            f"{item}=?" for item in parametrs
        ])
        return sql, tuple(parametrs.values())

    def select_user(self, **kwargs):
        sql = """SELECT * FROM Users WHERE """
        sql, parametrs = self.format_args(sql, kwargs)
        return self.execute(sql, parametrs=parametrs, fetchone=True)

    def count_users(self):
        sql = """SELECT COUNT(*) FROM Users"""
        return self.execute(sql, fetchone=True)

    def update_email(self, email, id):
        sql = """UPDATE Users SET email=? WHERE id=?"""
        return self.execute(sql, parametrs=(email, id), commit=True)

    def delete_users(self):
        sql = """DELETE FROM Users WHERE True"""
        self.execute(sql, commit=True)


def logger(statement):
    print(
        f"""
        ________________________________________________________________
        Execute:
        {statement}
        ________________________________________________________________
        """
    )
