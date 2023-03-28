"""setting up debug pt1

Revision ID: fc8312a0ec02
Revises: ee1b00ad5b91
Create Date: 2023-03-28 11:55:31.994904

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'fc8312a0ec02'
down_revision = 'ee1b00ad5b91'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('artists', sa.Column('genre', sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('artists', 'genre')
    # ### end Alembic commands ###
