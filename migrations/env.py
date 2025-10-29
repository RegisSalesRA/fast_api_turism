from logging.config import fileConfig

from sqlalchemy import engine_from_config
from sqlalchemy import pool

from alembic import context

from app.core.config import DATABASE_URL
from app.data.models.point_turism_model import Base
from app.data.models.category_model import Base
from app.data.models.city_model import Base

config = context.config
config.set_main_option('sqlalchemy.url',DATABASE_URL)

if config.config_file_name is not None:
    fileConfig(config.config_file_name) 

target_metadata = Base.metadata

def run_migrations_online() -> None:
    connectable = engine_from_config(
        config.get_section(config.config_ini_section, {}),
        prefix="sqlalchemy.",
        poolclass=pool.NullPool, 
    )
    with connectable.connect() as connection:
        context.configure(
            connection=connection, target_metadata=target_metadata
        )

        with context.begin_transaction():
            context.run_migrations()

run_migrations_online()