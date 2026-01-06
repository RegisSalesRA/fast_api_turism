"""Add created_at to all tables

Revision ID: e1f2g3h4i5j6
Revises: d4e5f6g7h8i9
Create Date: 2026-01-06 10:30:00.000000

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = 'e1f2g3h4i5j6'
down_revision = 'd4e5f6g7h8i9'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # Add created_at to favorites table
    op.add_column('favorites', sa.Column('created_at', sa.DateTime(timezone=True), server_default=sa.func.now(), nullable=False))
    
    # Add created_at to reviews table
    op.add_column('reviews', sa.Column('created_at', sa.DateTime(timezone=True), server_default=sa.func.now(), nullable=False))


def downgrade() -> None:
    # Remove created_at from reviews table
    op.drop_column('reviews', 'created_at')
    
    # Remove created_at from favorites table
    op.drop_column('favorites', 'created_at')
