import os

from sqlalchemy import text

from src.database.connection import engine


def setup_calendar():
    sql_path = os.path.join(os.path.dirname(__file__), "tables", "calendar.sql")

    with open(sql_path, "r") as f:
        sql = f.read()

    with engine.begin() as conn:
        conn.execute(text(sql))
        print("Tabela bcb.calendar criada com sucesso!")


if __name__ == "__main__":
    setup_calendar()
