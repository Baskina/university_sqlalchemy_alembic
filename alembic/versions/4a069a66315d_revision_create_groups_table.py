"""revision: create groups table

Revision ID: 4a069a66315d
Revises: 
Create Date: 2024-04-02 22:58:50.421289

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '4a069a66315d'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table("groups", sa.Column("id", sa.Integer(), primary_key=True, nullable=False, autoincrement=True),
                    sa.Column("name", sa.String(), nullable=False), )


def downgrade() -> None:
    op.drop_table("groups")
