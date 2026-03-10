# This file was created to run the application on heroku using gunicorn.
# Read more about it here: https://devcenter.heroku.com/articles/python-gunicorn

from app import app as application  # ✅ Importando la aplicación correctamente

if __name__ == "__main__":  # ✅ Comprobación correcta para ejecutar el script
    application.run()  # ✅ Ejecutando la aplicación correctamente
