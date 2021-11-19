"""add user table

Revision ID: 1ce6569b95be
Revises: 9408e579d445
Create Date: 2021-11-19 13:47:16.218859

"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = '1ce6569b95be'
down_revision = '9408e579d445'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('users',
                   sa.Column('id', sa.Integer(), nullable=False),
                   sa.Column('email', sa.String(), nullable=False),
                   sa.Column('password', sa.String(), nullable=False),
                   sa.Column('created_at', sa.TIMESTAMP(timezone=True),
                             server_default=sa.text('now()'), nullable=False),
                   sa.PrimaryKeyConstraint('id'),
                   sa.UniqueConstraint('email')
                   )
    pass


def downgrade():
    op.drop_table('users')
    pass
