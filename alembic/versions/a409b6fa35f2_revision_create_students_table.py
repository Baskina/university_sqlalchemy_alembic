"""revision: create students table

Revision ID: a409b6fa35f2
Revises: e1606a2b7a4e
Create Date: 2024-04-02 23:01:30.300635

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'a409b6fa35f2'
down_revision: Union[str, None] = 'e1606a2b7a4e'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table("students", sa.Column("id", sa.Integer(), primary_key=True, nullable=False, autoincrement=True),
                    sa.Column("name", sa.String(), nullable=False),
                    sa.Column("group_id", sa.Integer(), foreign_key=True, nullable=False),)


def downgrade() -> None:
    op.drop_table("students")
