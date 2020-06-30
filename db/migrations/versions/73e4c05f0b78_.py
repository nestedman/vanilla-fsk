"""empty message

Revision ID: 73e4c05f0b78
Revises: d3f98af4b0c7
Create Date: 2020-06-30 23:15:05.799310

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '73e4c05f0b78'
down_revision = 'd3f98af4b0c7'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('role_permissions', 'permission',
               existing_type=sa.VARCHAR(length=30),
               nullable=False)
    op.alter_column('role_permissions', 'role',
               existing_type=sa.VARCHAR(length=20),
               nullable=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('role_permissions', 'role',
               existing_type=sa.VARCHAR(length=20),
               nullable=True)
    op.alter_column('role_permissions', 'permission',
               existing_type=sa.VARCHAR(length=30),
               nullable=True)
    # ### end Alembic commands ###
