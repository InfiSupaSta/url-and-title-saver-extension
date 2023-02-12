import pathlib
import sqlite3
import pathlib

from .link import Link

BASE_DIR = pathlib.Path(__file__).parent.parent.parent
CUR_DIR = pathlib.Path(__file__).parent


class DatabasePreparation:

    def __init__(
            self,
            *,
            db_name: str = BASE_DIR.joinpath('db.sqlite3')
    ):
        self.db_name = db_name
        self.init_sql = 'init.sql'

    def get_init_sql(self):
        with open(CUR_DIR.joinpath(self.init_sql)) as sql:
            yield sql.read()

    def get_db_connect(self):
        return sqlite3.connect(self.db_name)

    def create_db(self):
        connect = self.get_db_connect()
        sql = self.get_init_sql()
        connect.execute(
            next(sql)
        )


class InsertRow:
    INSERT_SINGLE_ROW_SQL = f'INSERT INTO links(description, url) VALUES ("%s", "%s")'

    def __init__(self, db: sqlite3.Connection = DatabasePreparation().get_db_connect()):
        self.db = db

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is None:
            self.db.commit()
        else:
            self.db.rollback()

    def insert_row(self, data: Link) -> None:
        title = data.title
        url = data.url

        self.db.execute(
            self.INSERT_SINGLE_ROW_SQL % (title, url)
        )
