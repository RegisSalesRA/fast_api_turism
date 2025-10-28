import os
from dotenv import load_dotenv
from sqlalchemy.engine.url import URL

load_dotenv()

DATABASE = {
    "drivername": "postgresql+psycopg2",
    "username": os.getenv("DB_USER"),
    "password": os.getenv("DB_PASSWORD"),
    "host": os.getenv("DB_HOST"),
    "port": os.getenv("DB_PORT"),
    "database": os.getenv("DB_NAME"),
}

DATABASE_URL = str(URL.create(**DATABASE))
