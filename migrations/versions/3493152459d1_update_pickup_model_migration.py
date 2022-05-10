"""Update Pickup Model Migration

Revision ID: 3493152459d1
Revises: 62a950bfddb4
Create Date: 2022-05-10 11:12:07.663885

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3493152459d1'
down_revision = '62a950bfddb4'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('pickupLines',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('pickupLine', sa.String(), nullable=True),
    sa.Column('postedDate', sa.DateTime(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('pickupLines')
    # ### end Alembic commands ###
