from flask import Flask
from variables import conexion


app = Flask(__name__)
# print(app.config)
# app.config almacenara todas las variables que se utilizan en el proyecto de Flask
# NOTA: No confundir con las variables de entorno!
# ruta de sql
# dialecto://usuario:contraseña@host:puerto/base_de_datos ('mysql://root:root@host:3306/alumnos')

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:root@host:3306/alumnos'

# Inicializar la conexion de nuestra DB
# al momento de pasarle la aplicacion de flask en esta se encontraras la cadena de conexion a la DB

conexion.init_app(app)

if __name__ == '__main__':
    app.run(debug=True)