"""add foreign key

Revision ID: 70eff79bc3f7
Revises: e4fc0add14c9
Create Date: 2024-05-05 19:00:01.997313

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '70eff79bc3f7'
down_revision: Union[str, None] = 'e4fc0add14c9'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
