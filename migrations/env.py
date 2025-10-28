from app.core.config import DATABASE_URL  
from app.core.dependencies import Base
from alembic import context
from sqlalchemy import engine_from_config, pool

target_metadata = Base.metadata

def run_migrations_online():
    connectable = engine_from_config(
        {},
        prefix="",
        poolclass=pool.NullPool,
        url=DATABASE_URL
    )
    with connectable.connect() as connection:
        context.configure(connection=connection, target_metadata=target_metadata)
        with context.begin_transaction():
            context.run_migrations()
