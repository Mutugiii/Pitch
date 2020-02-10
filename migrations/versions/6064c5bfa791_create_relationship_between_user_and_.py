"""Create relationship between User and Roles

Revision ID: 6064c5bfa791
Revises: 028ff06f1c5f
Create Date: 2020-02-10 14:36:37.773396

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6064c5bfa791'
down_revision = '028ff06f1c5f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('role_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'users', 'roles', ['role_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'users', type_='foreignkey')
    op.drop_column('users', 'role_id')
    # ### end Alembic commands ###
