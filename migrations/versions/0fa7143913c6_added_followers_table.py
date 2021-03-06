"""Added followers table

Revision ID: 0fa7143913c6
Revises: 313115430b64
Create Date: 2021-03-15 17:42:53.649223

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0fa7143913c6'
down_revision = '313115430b64'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('followers',
    sa.Column('follower_id', sa.Integer(), nullable=True),
    sa.Column('followed_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['followed_id'], ['user.id'], ),
    sa.ForeignKeyConstraint(['follower_id'], ['user.id'], )
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('followers')
    # ### end Alembic commands ###
