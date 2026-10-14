import os
import time

import mysql.connector  # pyright: ignore[reportMissingImports]
from mysql.connector import Error  # pyright: ignore[reportMissingImports]


def connect_with_retry(attempts: int = 30, delay_seconds: int = 2):
    config = {
        "host": os.environ.get("DB_HOST", "db"),
        "port": int(os.environ.get("DB_PORT", "3306")),
        "database": os.environ["MYSQL_DATABASE"],
        "user": os.environ["MYSQL_USER"],
        "password": os.environ["MYSQL_PASSWORD"],
        "connection_timeout": 5,
    }
    for attempt in range(1, attempts + 1):
        try:
            return mysql.connector.connect(**config)
        except Error as exc:
            if attempt == attempts:
                raise RuntimeError(
                    f"Database was not reachable after {attempts} attempts"
                ) from exc
            print(f"Database not ready (attempt {attempt}/{attempts}); retrying...", flush=True)
            time.sleep(delay_seconds)


def main() -> None:
    connection = connect_with_retry()
    try:
        with connection.cursor() as cursor:
            cursor.execute("SELECT DATABASE(), VERSION()")
            database, version = cursor.fetchone()
            print(f"Connected to database {database} on MySQL {version}")
    finally:
        connection.close()


if __name__ == "__main__":
    main()
