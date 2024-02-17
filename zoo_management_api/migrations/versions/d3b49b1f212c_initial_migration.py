from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

revision = 'd3b49b1f212c'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('animals',
    sa.Column('id', sa.UUID(), nullable=False),
    sa.Column('species', sa.String(length=50), nullable=False),
    sa.Column('age', sa.Integer(), nullable=False),
    sa.Column('gender', sa.String(length=10), nullable=False),
    sa.Column('special_requirement', sa.String(length=200), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('id')
    )
    op.create_table('employees',
    sa.Column('id', sa.UUID(), nullable=False),
    sa.Column('name', sa.String(length=100), nullable=False),
    sa.Column('email', sa.String(length=100), nullable=False),
    sa.Column('phone_number', sa.String(length=20), nullable=False),
    sa.Column('role', sa.String(length=50), nullable=False),
    sa.Column('schedule', sa.String(length=200), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('id')
    )
    op.drop_table('animal')

def downgrade():
    op.create_table('animal',
    sa.Column('id', sa.UUID(), server_default=sa.text('gen_random_uuid()'), autoincrement=False, nullable=False),
    sa.Column('created_at', postgresql.TIMESTAMP(timezone=True), server_default=sa.text('now()'), autoincrement=False, nullable=False),
    sa.Column('species', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('age', sa.BIGINT(), autoincrement=False, nullable=True),
    sa.Column('gender', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('special_requirement', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('id', name='animal_pkey')
    )
    op.drop_table('employees')
    op.drop_table('animals')
