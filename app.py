from flask import Flask, request
from variables import conexion
from models.usuario import UsuarioModel
from models.direcciones import DireccionModel
from flask_migrate import Migrate
from datetime import datetime


app = Flask(__name__)
# print(app.config)
# app.config almacenara todas las variables que se utilizan en el proyecto de Flask
# NOTA: No confundir con las variables de entorno!
# ruta de sql
# dialecto://usuario:contraseña@host:puerto/base_de_datos ('mysql://root:root@host:3306/alumnos')

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:root@localhost:3306/alumnos'

# Inicializar la conexion de nuestra DB
# al momento de pasarle la aplicacion de flask en esta se encontraras la cadena de conexion a la DB

conexion.init_app(app)

# Migrate sirve para comenzr a registrar los cambios en nuestra base de datos realizados desde nuestra ORM
Migrate(app=app, db=conexion)

# # before_request > se mandara a llamar a esta funcionabilidad antes de cualquier request (peticion)
# @app.before_request
# def inicializacion():
# drop_all() > elimina todas las tablas y sus datos y perdemos la informacion
# # create_all > crea todas las tablas que no se han creado en la base de datos
#     conexion.create_all()

@app.route('/usuarios', methods=['GET'])
def gestionarUsuarios():
    # session > una actividad que tenemos con la base de datos
    # SELECT * FROM usuarios;
    resultado = conexion.session.query(UsuarioModel).all()
    # print(resultado[0].nombre)

    usuarios = []
    for usuario in resultado:
        usuarios.append({
            'id':usuario.id,
            'nombre':usuario.nombre,
            'apellido':usuario.apellido,
            # string for time (strftime) > convierte un valor tipo fecha y hora a estring pero colocando el formato
            # %Y > devolvera el año
            # %y > devuelve los 2 ultimos digitos del año
            # %m > devuelve los digitos del mes
            # %B > devuelve el nombre del mes
            # %b > devuelve las tres primeras letras del mes
            # %d > devuelve el dia del mes
            # %H > devuelve la hora
            # %M > devuelve minutos 
            # %S > devuelve segundos
            'fechaNacimiento':datetime.strftime(usuario.fechaNacimiento, '%Y-%m-%d'),
            'sexo':usuario.sexo
        })
    
    print(usuarios)

    
    return {
        'content': usuarios
    }, 200

@app.route('/usuario', methods=['POST'])
def crearUsuario():
    # Capturar la informacion
    try:
        data = request.get_json()

        # Crear nuevo usuario
        nuevoUsuario = UsuarioModel (
                                    nombre = data.get('nombre'),
                                    apellido = data.get('apellido'),
                                    correo = data.get('correo'),
                                    sexo = data.get('sexo'),
                                    fechaNacimiento = data.get('fechaNacimiento')
        )

        # Agregar este nuevo registro a la base de datos de manera temporal
        conexion.session.add(nuevoUsuario)

        print('Antes del commit', nuevoUsuario.id)

        # commit sirve para transacciones y pasarle que todos los cambios realizados en la base de dtos permanexcan de manera permanente 
        conexion.session.commit()

        print('Despues de commit', nuevoUsuario.id)

        return {
            'message': 'Usuario creado exitosamente'
        }, 201
    except Exception as error:
        return {
            'message': 'Error al crear el usuario',
            'content': error.args
        }
    

@app.route('/')
def inicial():
    return {
        'message':'Bienvenido a mi API de usuarios'
    }

if __name__ == '__main__':
    app.run(debug=True)