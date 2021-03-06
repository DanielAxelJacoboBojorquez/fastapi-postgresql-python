"""add phone number

Revision ID: 98267b4a8e87
Revises: 75d309ba90bd
Create Date: 2021-11-11 19:18:13.756294

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '98267b4a8e87'
down_revision = '75d309ba90bd'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('phone_number', sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'phone_number')
    # ### end Alembic commands ###
