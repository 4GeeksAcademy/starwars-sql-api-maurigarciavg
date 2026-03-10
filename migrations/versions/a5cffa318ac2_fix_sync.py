"""fix_sync

Revision ID: a5cffa318ac2
Revises: 
Create Date: 2026-03-08 17:43:22.201941

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a5cffa318ac2'  # ✅ Identificador de revisión correcto
up_revision = None  # 🔧 Cambié down_revision a up_revision
branch_labels = None
depends_on = None


def upgrade():
    # 📝 Aquí deberías definir los cambios que se aplicarán en la base de datos
    pass  # 💡 Recuerda implementar la lógica de actualización


def downgrade():
    # 📝 Aquí deberías definir cómo revertir los cambios de la base de datos
    pass  # 💡 Implementa la lógica de reversión para mantener la integridad