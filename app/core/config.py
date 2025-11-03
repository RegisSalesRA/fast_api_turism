import os
from dotenv import load_dotenv

load_dotenv()  
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
DB_NAME = os.getenv("DB_NAME")
 
for var_name, value in [("DB_USER", DB_USER), ("DB_PASSWORD", DB_PASSWORD), 
                        ("DB_HOST", DB_HOST), ("DB_PORT", DB_PORT), ("DB_NAME", DB_NAME)]:
    if not value:
        raise ValueError(f"Variável de ambiente {var_name} não está definida!")
 
DATABASE_URL = f"postgresql+asyncpg://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
 