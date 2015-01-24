"""empty message

Revision ID: 4c15ae50b120
Revises: 180ec1bd526d
Create Date: 2015-01-16 10:46:30.555573

"""

# revision identifiers, used by Alembic.
revision = '4c15ae50b120'
down_revision = '180ec1bd526d'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('crawl_model',
            sa.Column('id', sa.Integer(), nullable=False),
            sa.Column('name', sa.Text(), nullable=True),
            sa.Column('project_id', sa.Integer(), nullable=True),
            sa.ForeignKeyConstraint(['project_id'], ['project.id'], ),
            sa.PrimaryKeyConstraint('id'),
            sa.UniqueConstraint('name')
            )
    naming_convention = {
        "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
    }
    with op.batch_alter_table("crawl", naming_convention=naming_convention) as batch_op:
        batch_op.add_column(sa.Column('crawl_model_id', sa.Integer(), nullable=True))
        batch_op.drop_constraint('fk_crawl_data_model_id_data_model', type_='foreignkey')
        batch_op.create_foreign_key('crawl', 'crawl_model', ['crawl_model_id'], ['id'])
        batch_op.drop_column('data_model_id')
    op.drop_table('data_model')
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('data_model',
            sa.Column('id', sa.INTEGER(), nullable=False),
            sa.Column('name', sa.TEXT(), nullable=True),
            sa.Column('project_id', sa.INTEGER(), nullable=True),
            sa.ForeignKeyConstraint(['project_id'], [u'project.id'], ),
            sa.PrimaryKeyConstraint('id')
            )
    naming_convention = {
        "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
    }
    with op.batch_alter_table("crawl", naming_convention=naming_convention) as batch_op:
        batch_op.add_column(sa.Column('data_model_id', sa.INTEGER(), nullable=True))
        batch_op.drop_constraint('fk_crawl_crawl_model_id_crawl_model', type_='foreignkey')
        batch_op.create_foreign_key('crawl', 'data_model', ['data_model_id'], ['id'])
        batch_op.drop_column('crawl_model_id')
    op.drop_table('crawl_model')
    ### end Alembic commands ###

