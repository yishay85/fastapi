"""creat posts table

Revision ID: 745e05410670
Revises: 
Create Date: 2021-11-19 13:24:23.689505

"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = '745e05410670'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_column('posts', sa.Column('id', sa.Integer(), nullable=False, primary_key=True),
                     sa.Column('title', sa.String(), nullable=False))
    pass


def downgrade():
    op.drop_column('posts')
    pass
