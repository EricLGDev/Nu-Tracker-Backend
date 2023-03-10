"""empty message

Revision ID: 5229e84b602f
Revises: a42ee9734afb
Create Date: 2023-02-12 12:13:46.608009

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5229e84b602f'
down_revision = 'a42ee9734afb'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('food', schema=None) as batch_op:
        batch_op.drop_constraint('food_name_key', type_='unique')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('food', schema=None) as batch_op:
        batch_op.create_unique_constraint('food_name_key', ['name'])

    # ### end Alembic commands ###
