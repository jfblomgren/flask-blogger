"""empty message

Revision ID: 127b78fa140
Revises: 1169ddd19aa
Create Date: 2015-12-23 14:41:32.280656

"""

# revision identifiers, used by Alembic.
revision = '127b78fa140'
down_revision = '1169ddd19aa'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('post', sa.Column('long_text', sa.String(length=10000), nullable=True))
    op.add_column('post', sa.Column('short_text', sa.String(length=1000), nullable=True))
    op.drop_column('post', 'body')
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('post', sa.Column('body', sa.VARCHAR(length=10000), autoincrement=False, nullable=False))
    op.drop_column('post', 'short_text')
    op.drop_column('post', 'long_text')
    ### end Alembic commands ###
