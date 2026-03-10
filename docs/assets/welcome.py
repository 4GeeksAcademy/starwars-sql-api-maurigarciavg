print("""


WELCOME GEEK! 🐍 + 💻 = 🤓

The server is already running, \033[94mctr + c\033[0m to stop the server if you like

The following commands are available to run your code:

- \033[94m$ pipenv run migrate\033[0m create database migrations (if models.py is edited)
- \033[94m$ pipenv run upgrade\033[0m run database migrations (if pending)
- \033[94m$ pipenv run start\033[0m start flask web server (if not running)
- \033[94m$ pipenv run deploy\033[0m deploy to heroku (if needed) \n\n
""") // ✅ Buen uso de print para mostrar información al usuario.
// 💡 Considera usar una función para encapsular este código y hacerlo más modular.
// 🔧 Asegúrate de que el código esté correctamente indentado y no tenga errores de sintaxis.