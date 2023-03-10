"""empty message

Revision ID: a42ee9734afb
Revises: 1ef82ba45a6e
Create Date: 2023-02-12 11:39:47.882390

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a42ee9734afb'
down_revision = '1ef82ba45a6e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('log_food')
    op.drop_table('calorie_intake')
    with op.batch_alter_table('food', schema=None) as batch_op:
        batch_op.add_column(sa.Column('user_id', sa.Integer(), nullable=False))
        batch_op.create_foreign_key(None, 'users', ['user_id'], ['id'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('food', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.drop_column('user_id')

    op.create_table('calorie_intake',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('food', sa.VARCHAR(length=50), autoincrement=False, nullable=False),
    sa.Column('calories', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('user_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('date', sa.DATE(), autoincrement=False, nullable=False),
    sa.Column('fat', sa.DOUBLE_PRECISION(precision=53), autoincrement=False, nullable=False),
    sa.Column('protein', sa.DOUBLE_PRECISION(precision=53), autoincrement=False, nullable=False),
    sa.Column('carbohydrates', sa.DOUBLE_PRECISION(precision=53), autoincrement=False, nullable=False),
    sa.Column('sodium', sa.DOUBLE_PRECISION(precision=53), autoincrement=False, nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], name='calorie_intake_user_id_fkey'),
    sa.PrimaryKeyConstraint('id', name='calorie_intake_pkey')
    )
    op.create_table('log_food',
    sa.Column('users_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('food_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.ForeignKeyConstraint(['food_id'], ['food.id'], name='log_food_food_id_fkey'),
    sa.ForeignKeyConstraint(['users_id'], ['users.id'], name='log_food_users_id_fkey'),
    sa.PrimaryKeyConstraint('users_id', 'food_id', name='log_food_pkey')
    )
    # ### end Alembic commands ###
