"""add content column

Revision ID: 54662b4c55e2
Revises: 2527e414f41c
Create Date: 2024-05-05 18:38:58.197042

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '54662b4c55e2'
down_revision: Union[str, None] = '2527e414f41c'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('posts',sa.Column('content',sa.String(),nullable=False))
    pass


def downgrade() -> None:
    pass
