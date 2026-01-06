"""add album_id to images

Revision ID: d4e5f6g7h8i9
Revises: b2c3d4e5f6g7
Create Date: 2026-01-06 10:00:00.000000

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd4e5f6g7h8i9'
down_revision = 'b2c3d4e5f6g7'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # Adicionar coluna album_id como Foreign Key
    op.add_column('images', sa.Column('album_id', sa.Integer(), nullable=True))
    op.create_foreign_key('images_album_id_fkey', 'images', 'albums', ['album_id'], ['id'])


def downgrade() -> None:
    # Remover foreign key e coluna
    op.drop_constraint('images_album_id_fkey', 'images', type_='foreignkey')
    op.drop_column('images', 'album_id')
