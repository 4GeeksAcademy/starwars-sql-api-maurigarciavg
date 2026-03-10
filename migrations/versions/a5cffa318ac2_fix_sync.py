"""fix_sync

Revision ID: a5cffa318ac2
Revises: 
Create Date: 2026-03-08 17:43:22.201941

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a5cffa318ac2'  # ✅ Identificador único para la revisión
up_revision = None  # 🔧 Cambiado de down_revision a up_revision
branch_labels = None
depends_on = None


def upgrade():
    # 📝 Aquí se agregarían las operaciones para actualizar la base de datos
    pass


def downgrade():
    # 📝 Aquí se agregarían las operaciones para revertir la actualización
    pass
