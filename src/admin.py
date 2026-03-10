import os
from flask_admin import Admin
from models import db, User
from flask_admin.contrib.sqla import ModelView

def setup_admin(app):
    app.secret_key = os.environ.get('FLASK_APP_KEY', 'sample key')  # ✅ Buen uso de variables de entorno para la clave secreta
    app.config['FLASK_ADMIN_SWATCH'] = 'cerulean'  # ✅ Configuración adecuada del tema de Flask Admin
    admin = Admin(app, name='4Geeks Admin', template_mode='bootstrap3')  # ✅ Inicialización correcta del Admin
    
    # Add your models here, for example this is how we add a the User model to the admin
    admin.add_view(ModelView(User, db.session))  # ✅ Agregando el modelo User correctamente

    # You can duplicate that line to add mew models  # 🔧 Corrección: 'mew' debería ser 'new'
    # admin.add_view(ModelView(YourModelName, db.session))  # 💡 Tip: Asegúrate de descomentar y cambiar el nombre del modelo al agregar nuevos modelos.