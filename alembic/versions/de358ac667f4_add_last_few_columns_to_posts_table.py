"""add last few columns to posts table

Revision ID: de358ac667f4
Revises: 57bdaa99e097
Create Date: 2021-11-19 15:00:44.905324

"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = 'de358ac667f4'
down_revision = '57bdaa99e097'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', sa.Column(
        'published', sa.Boolean(), nullable=False, server_default='TRUE'), )
    op.add_column('posts', sa.Column(
        'created_at', sa.TIMESTAMP(timezone=True), nullable=False, server_default=sa.text('NOW()')), )
    pass


def downgrade():
    op.drop_column('posts', 'published')
    op.drop_column('posts', 'created_at')
    pass
