"""empty message

Revision ID: fda94c1f436c
Revises: 3cd053740d8b
Create Date: 2019-04-06 14:20:52.745907

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'fda94c1f436c'
down_revision = '3cd053740d8b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('reports',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('order_id', sa.Integer(), nullable=False),
    sa.Column('user_firstName', sa.String(length=24), nullable=False),
    sa.Column('user_secondName', sa.String(length=24), nullable=False),
    sa.Column('user_status', sa.Integer(), nullable=False),
    sa.Column('employee_feedback', sa.TEXT(length=1000)),
    sa.Column('user_id', sa.Integer()),
    sa.Column('employee_id', sa.Integer()),
    sa.Column('report_describe'),
    sa.Column('create_time', sa.TIMESTAMP(), nullable=False),
    sa.ForeignKeyConstraint(['employee_id'], ['employees.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('reports')
    # ### end Alembic commands ###
