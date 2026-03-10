import os
from flask_admin import Admin
from models import db, User
from flask_admin.contrib.sqla import ModelView

def setup_admin(app):
    app.secret_key = os.environ.get('FLASK_APP_KEY', 'sample key')  # ✅ Buen uso de variables de entorno
    app.config['FLASK_ADMIN_SWATCH'] = 'cerulean'  # ✅ Configuración correcta del tema
    admin = Admin(app, name='4Geeks Admin', template_mode='bootstrap3')  # ✅ Inicialización del Admin correcta
    
    # Add your models here, for example this is how we add a the User model to the admin
    admin.add_view(ModelView(User, db.session))  # ✅ Agregar modelo User correctamente

    # You can duplicate that line to add mew models
    # admin.add_view(ModelView(YourModelName, db.session))  # 💡 Recuerda que puedes agregar más modelos aquí