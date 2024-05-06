"""create posts table

Revision ID: 2527e414f41c
Revises: 
Create Date: 2024-05-05 16:59:19.763017

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '2527e414f41c'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    op.create_table('posts', sa.Column('id', sa.Integer(), nullable=False,
                    primary_key=True), sa.Column('title', sa.String(), nullable=False))
    pass


def downgrade():
    op.drop_table('posts')
    pass