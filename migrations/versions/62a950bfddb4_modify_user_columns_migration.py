"""Modify User Columns Migration

Revision ID: 62a950bfddb4
Revises: 9afff8156721
Create Date: 2022-05-09 19:34:35.719431

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '62a950bfddb4'
down_revision = '9afff8156721'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('emails', sa.String(length=255), nullable=True))
    op.add_column('users', sa.Column('usernames', sa.String(length=255), nullable=True))
    op.add_column('users', sa.Column('password_hashes', sa.String(length=255), nullable=True))
    op.drop_index('ix_users_email', table_name='users')
    op.drop_index('ix_users_username', table_name='users')
    op.create_index(op.f('ix_users_emails'), 'users', ['emails'], unique=True)
    op.create_index(op.f('ix_users_usernames'), 'users', ['usernames'], unique=True)
    op.drop_column('users', 'email')
    op.drop_column('users', 'password')
    op.drop_column('users', 'username')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('username', sa.VARCHAR(length=255), autoincrement=False, nullable=True))
    op.add_column('users', sa.Column('password', sa.VARCHAR(length=255), autoincrement=False, nullable=True))
    op.add_column('users', sa.Column('email', sa.VARCHAR(length=255), autoincrement=False, nullable=True))
    op.drop_index(op.f('ix_users_usernames'), table_name='users')
    op.drop_index(op.f('ix_users_emails'), table_name='users')
    op.create_index('ix_users_username', 'users', ['username'], unique=False)
    op.create_index('ix_users_email', 'users', ['email'], unique=False)
    op.drop_column('users', 'password_hashes')
    op.drop_column('users', 'usernames')
    op.drop_column('users', 'emails')
    # ### end Alembic commands ###
