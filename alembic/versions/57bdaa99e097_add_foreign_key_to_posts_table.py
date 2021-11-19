"""add foreign-key to posts table

Revision ID: 57bdaa99e097
Revises: 1ce6569b95be
Create Date: 2021-11-19 14:39:42.241454

"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = '57bdaa99e097'
down_revision = '1ce6569b95be'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', sa.Column("owner_id", sa.Integer(), nullable=False))
    op.create_foreign_key('posts_users_fk', source_table="posts", referent_table="users", local_cols=['owner_id'],
                          remote_cols=['id'], ondelete="CASCADE")
    pass


def downgrade():
    op.drop_constraint('posts_users_fk',table_name='posts')
    op.drop_column('posts','owner_id')
    pass
