# This file was created to run the application on heroku using gunicorn.
# Read more about it here: https://devcenter.heroku.com/articles/python-gunicorn

from app import app as application  # ✅ Importación correcta de la aplicación

if __name__ == "__main__":  # ✅ Comprobación correcta para ejecutar el script
    application.run()  # ✅ Método para ejecutar la aplicación
