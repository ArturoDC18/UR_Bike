"""empty message

Revision ID: 0eed5d06290d
Revises: 654a3b0fbed7
Create Date: 2024-11-17 00:01:03.622383

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0eed5d06290d'
down_revision = '654a3b0fbed7'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('bike_part', schema=None) as batch_op:
        batch_op.add_column(sa.Column('price', sa.Float(), nullable=True))
        batch_op.add_column(sa.Column('buy_link', sa.String(length=200), nullable=True))
        batch_op.add_column(sa.Column('category', sa.String(length=100), nullable=True))
        batch_op.alter_column('description',
               existing_type=sa.TEXT(),
               type_=sa.String(length=200),
               nullable=True)
        batch_op.drop_column('where_to_buy')
        batch_op.drop_column('how_to_fix')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('bike_part', schema=None) as batch_op:
        batch_op.add_column(sa.Column('how_to_fix', sa.TEXT(), nullable=False))
        batch_op.add_column(sa.Column('where_to_buy', sa.TEXT(), nullable=False))
        batch_op.alter_column('description',
               existing_type=sa.String(length=200),
               type_=sa.TEXT(),
               nullable=False)
        batch_op.drop_column('category')
        batch_op.drop_column('buy_link')
        batch_op.drop_column('price')

    # ### end Alembic commands ###