"""empty message

Revision ID: 3890f70717a
Revises: 48df0aff185
Create Date: 2015-12-25 17:33:33.295851

"""

# revision identifiers, used by Alembic.
revision = '3890f70717a'
down_revision = '48df0aff185'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('tag', sa.Column('slug', sa.String(length=80), nullable=True))
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('tag', 'slug')
    ### end Alembic commands ###