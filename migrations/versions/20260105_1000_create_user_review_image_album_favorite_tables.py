"""create tables for user, review, image, album and favorite

Revision ID: a1b2c3d4e5f6
Revises: a2b3c4d5e6f7
Create Date: 2026-01-05 10:00:00.000000

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a1b2c3d4e5f6'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # Create users table
    op.create_table(
        'users',
        sa.Column('id', sa.String(36), nullable=False),
        sa.Column('name', sa.String(255), nullable=False),
        sa.Column('email', sa.String(255), nullable=False),
        sa.Column('role', sa.Enum('USER', 'ADMIN', name='userrole'), nullable=False, server_default='USER'),
        sa.Column('created_at', sa.DateTime(timezone=True), server_default=sa.func.now(), nullable=False),
        sa.Column('last_login', sa.DateTime(timezone=True), nullable=True),
        sa.Column('updated_at', sa.DateTime(timezone=True), server_default=sa.func.now(), onupdate=sa.func.now(), nullable=False),
        sa.PrimaryKeyConstraint('id'),
        sa.UniqueConstraint('email', name='uq_users_email'),
    )
    op.create_index(op.f('ix_users_id'), 'users', ['id'], unique=False)
    op.create_index(op.f('ix_users_email'), 'users', ['email'], unique=False)

    # Create images table
    op.create_table(
        'images',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('url', sa.String(500), nullable=False),
        sa.Column('created_at', sa.DateTime(timezone=True), server_default=sa.func.now(), nullable=False),
        sa.Column('updated_at', sa.DateTime(timezone=True), server_default=sa.func.now(), onupdate=sa.func.now(), nullable=False),
        sa.PrimaryKeyConstraint('id'),
    )
    op.create_index(op.f('ix_images_id'), 'images', ['id'], unique=False)

    # Create albums table
    op.create_table(
        'albums',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('title', sa.String(255), nullable=False),
        sa.Column('description', sa.String(1000), nullable=True),
        sa.Column('created_at', sa.DateTime(timezone=True), server_default=sa.func.now(), nullable=False),
        sa.Column('updated_at', sa.DateTime(timezone=True), server_default=sa.func.now(), onupdate=sa.func.now(), nullable=False),
        sa.PrimaryKeyConstraint('id'),
    )
    op.create_index(op.f('ix_albums_id'), 'albums', ['id'], unique=False)

    # Create album_images association table
    op.create_table(
        'album_images',
        sa.Column('album_id', sa.Integer(), nullable=False),
        sa.Column('image_id', sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(['album_id'], ['albums.id'], ),
        sa.ForeignKeyConstraint(['image_id'], ['images.id'], ),
        sa.PrimaryKeyConstraint('album_id', 'image_id'),
    )

    # Create reviews table
    op.create_table(
        'reviews',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('user_id', sa.String(36), nullable=False),
        sa.Column('point_turism_id', sa.Integer(), nullable=False),
        sa.Column('rating', sa.Float(), nullable=False),
        sa.Column('comment', sa.String(1000), nullable=True),
        sa.Column('created_at', sa.DateTime(timezone=True), server_default=sa.func.now(), nullable=False),
        sa.Column('updated_at', sa.DateTime(timezone=True), server_default=sa.func.now(), onupdate=sa.func.now(), nullable=False),
        sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
        sa.ForeignKeyConstraint(['point_turism_id'], ['point_turisms.id'], ),
        sa.PrimaryKeyConstraint('id'),
    )
    op.create_index(op.f('ix_reviews_id'), 'reviews', ['id'], unique=False)

    # Create favorites table
    op.create_table(
        'favorites',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('user_id', sa.String(36), nullable=False),
        sa.Column('point_turism_id', sa.Integer(), nullable=False),
        sa.Column('created_at', sa.DateTime(timezone=True), server_default=sa.func.now(), nullable=False),
        sa.Column('updated_at', sa.DateTime(timezone=True), server_default=sa.func.now(), onupdate=sa.func.now(), nullable=False),
        sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
        sa.ForeignKeyConstraint(['point_turism_id'], ['point_turisms.id'], ),
        sa.PrimaryKeyConstraint('id'),
        sa.UniqueConstraint('user_id', 'point_turism_id', name='uq_user_point_turism'),
    )
    op.create_index(op.f('ix_favorites_id'), 'favorites', ['id'], unique=False)


def downgrade() -> None:
    # Drop favorites table
    op.drop_index(op.f('ix_favorites_id'), table_name='favorites')
    op.drop_table('favorites')

    # Drop reviews table
    op.drop_index(op.f('ix_reviews_id'), table_name='reviews')
    op.drop_table('reviews')

    # Drop album_images association table
    op.drop_table('album_images')

    # Drop albums table
    op.drop_index(op.f('ix_albums_id'), table_name='albums')
    op.drop_table('albums')

    # Drop images table
    op.drop_index(op.f('ix_images_id'), table_name='images')
    op.drop_table('images')

    # Drop users table
    op.drop_index(op.f('ix_users_email'), table_name='users')
    op.drop_index(op.f('ix_users_id'), table_name='users')
    op.drop_table('users')
