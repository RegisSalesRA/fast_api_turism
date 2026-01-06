"""add image_id to point_turisms

Revision ID: b2c3d4e5f6g7
Revises: a1b2c3d4e5f6
Create Date: 2026-01-05 11:00:00.000000

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b2c3d4e5f6g7'
down_revision = 'a1b2c3d4e5f6'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # Remove a coluna 'image' antiga (string)
    op.drop_column('point_turisms', 'image')
    
    # Adicionar coluna image_id como Foreign Key
    op.add_column('point_turisms', sa.Column('image_id', sa.Integer(), nullable=True))
    
    # Criar foreign key
    op.create_foreign_key('point_turisms_image_id_fkey', 'point_turisms', 'images', ['image_id'], ['id'])


def downgrade() -> None:
    # Remover foreign key
    op.drop_constraint('point_turisms_image_id_fkey', 'point_turisms', type_='foreignkey')
    
    # Remover coluna
    op.drop_column('point_turisms', 'image_id')
    
    # Adicionar coluna antiga de volta
    op.add_column('point_turisms', sa.Column('image', sa.String(length=255), nullable=False))
