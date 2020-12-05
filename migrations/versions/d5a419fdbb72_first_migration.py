"""first migration

Revision ID: d5a419fdbb72
Revises: 
Create Date: 2020-12-01 21:57:38.104543

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd5a419fdbb72'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('comment',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('author', sa.String(length=64), nullable=True),
    sa.Column('text', sa.String(length=256), nullable=True),
    sa.Column('timestamp', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_comment_author'), 'comment', ['author'], unique=False)
    op.create_index(op.f('ix_comment_id'), 'comment', ['id'], unique=False)
    op.create_index(op.f('ix_comment_text'), 'comment', ['text'], unique=False)
    op.create_index(op.f('ix_comment_timestamp'), 'comment', ['timestamp'], unique=False)
    op.create_table('img',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('file_name', sa.Text(), nullable=True),
    sa.Column('mimetype', sa.Text(), nullable=False),
    sa.Column('timestamp', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_img_file_name'), 'img', ['file_name'], unique=False)
    op.create_index(op.f('ix_img_id'), 'img', ['id'], unique=False)
    op.create_index(op.f('ix_img_timestamp'), 'img', ['timestamp'], unique=False)
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=64), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_user_id'), 'user', ['id'], unique=False)
    op.create_index(op.f('ix_user_username'), 'user', ['username'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_user_username'), table_name='user')
    op.drop_index(op.f('ix_user_id'), table_name='user')
    op.drop_table('user')
    op.drop_index(op.f('ix_img_timestamp'), table_name='img')
    op.drop_index(op.f('ix_img_id'), table_name='img')
    op.drop_index(op.f('ix_img_file_name'), table_name='img')
    op.drop_table('img')
    op.drop_index(op.f('ix_comment_timestamp'), table_name='comment')
    op.drop_index(op.f('ix_comment_text'), table_name='comment')
    op.drop_index(op.f('ix_comment_id'), table_name='comment')
    op.drop_index(op.f('ix_comment_author'), table_name='comment')
    op.drop_table('comment')
    # ### end Alembic commands ###
