"""add users table

Revision ID: e4fc0add14c9
Revises: 54662b4c55e2
Create Date: 2024-05-05 18:43:50.116210

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'e4fc0add14c9'
down_revision: Union[str, None] = '54662b4c55e2'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table('users',sa.Column('id',sa.Integer(),nullable=False),
                    sa.Column('email',sa.String(),nullable=False),
                    sa.Column('password',sa.String(),nullable=False),
                    sa.PrimaryKeyConstraint('id'),
                    sa.UniqueConstraint('email'))
    pass


def downgrade() -> None:
    pass
