"""add content column to post table

Revision ID: 9408e579d445
Revises: 745e05410670
Create Date: 2021-11-19 13:38:20.158401

"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = '9408e579d445'
down_revision = '745e05410670'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade():
    op.drop_column('posts', 'content')
    pass
