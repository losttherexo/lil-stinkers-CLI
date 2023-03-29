"""gave stream table a name column

Revision ID: fbcb4591a47d
Revises: 2dc9f6dfcf55
Create Date: 2023-03-29 17:05:16.083600

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'fbcb4591a47d'
down_revision = '2dc9f6dfcf55'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('streams', sa.Column('song_name', sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('streams', 'song_name')
    # ### end Alembic commands ###