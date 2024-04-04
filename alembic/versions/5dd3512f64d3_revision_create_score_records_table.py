"""revision: create score_records table

Revision ID: 5dd3512f64d3
Revises: a7c53da6c43f
Create Date: 2024-04-02 23:08:04.042532

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '5dd3512f64d3'
down_revision: Union[str, None] = 'a7c53da6c43f'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table("score_records", sa.Column("id", sa.Integer(), primary_key=True, nullable=False, autoincrement=True),
                    sa.Column("student_id", sa.Integer(), sa.ForeignKey("students.id"), nullable=False),
                    sa.Column("subject_id", sa.Integer(), sa.ForeignKey("subjects.id"), nullable=False),
                    sa.Column("score", sa.Integer(), nullable=False),
                    sa.Column("date", sa.DateTime(), nullable=False), )


def downgrade() -> None:
    op.drop_table("score_records")
