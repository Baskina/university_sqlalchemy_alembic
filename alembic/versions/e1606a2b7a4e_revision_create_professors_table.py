"""revision: create professors table

Revision ID: e1606a2b7a4e
Revises: 4a069a66315d
Create Date: 2024-04-02 23:00:14.204744

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'e1606a2b7a4e'
down_revision: Union[str, None] = '4a069a66315d'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table("professors", sa.Column("id", sa.Integer(), primary_key=True, nullable=False, autoincrement=True),
                    sa.Column("name", sa.String(), nullable=False), )


def downgrade() -> None:
    op.drop_table("professors")
