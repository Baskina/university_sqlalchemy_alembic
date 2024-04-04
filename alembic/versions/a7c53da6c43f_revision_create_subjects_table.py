"""revision: create subjects table

Revision ID: a7c53da6c43f
Revises: a409b6fa35f2
Create Date: 2024-04-02 23:06:32.939662

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'a7c53da6c43f'
down_revision: Union[str, None] = 'a409b6fa35f2'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table("subjects", sa.Column("id", sa.Integer(), primary_key=True, nullable=False, autoincrement=True),
                    sa.Column("title", sa.String(), nullable=False),
                    sa.Column("professor_id", sa.Integer(), sa.ForeignKey("professors.id"), nullable=False),)
    pass


def downgrade() -> None:
    op.drop_table("subjects")
