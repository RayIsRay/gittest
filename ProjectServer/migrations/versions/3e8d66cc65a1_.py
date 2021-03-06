"""empty message

Revision ID: 3e8d66cc65a1
Revises: ee609d85c1d2
Create Date: 2019-04-29 10:45:25.277893

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3e8d66cc65a1'
down_revision = 'ee609d85c1d2'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('insurances',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('create_time', sa.TIMESTAMP(), nullable=False),
    sa.Column('insurance_start', sa.DATETIME(), nullable=False),
    sa.Column('insurance_end', sa.DATETIME(), nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('insurances')
    # ### end Alembic commands ###
