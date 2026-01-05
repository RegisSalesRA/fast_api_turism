from logging.config import fileConfig

from alembic import context
from sqlalchemy import engine_from_config, pool

from app.core.config import SYNC_DATABASE_URL
from app.db.base import Base

# IMPORTANTE: importa os models para registrar no metadata
from app.data.models import city_model
from app.data.models import category_model
from app.data.models import point_turism_model

config = context.config

if config.config_file_name is not None:
    fileConfig(config.config_file_name)

# ALEMBIC SEMPRE SYNC
config.set_main_option("sqlalchemy.url", SYNC_DATABASE_URL)

target_metadata = Base.metadata


def run_migrations_online() -> None:
    connectable = engine_from_config(
        config.get_section(config.config_ini_section),
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )

    with connectable.connect() as connection:
        context.configure(
            connection=connection,
            target_metadata=target_metadata,
            compare_type=True,
        )

        with context.begin_transaction():
            context.run_migrations()


run_migrations_online()
