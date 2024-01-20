from flask import Flask, request
from uuid import uuid4
from flask_cors import CORS

app = Flask(__name__)

# Para configurar mis CORS lo hago de la siguiente manera
# Si lo dejamos sin ninguna configuracion adicional lo que va a suceder es que en teoria va a permitir que todos los origenes y todos los metodos y todos los headers sean permitidos 
CORS(app=app, 
     # Que metodos puedem acceder a mi API
     methods=['GET', 'POST', 'PUT', 'DELETE'],
     # Desde que dominios se puede acceder a mi API, si queremos que cualquier origen se conecte, colocamos el '*'
     origins=['http://localhost:5500', 'http://127.0.0.1:5500'],
     # Que headers (cabeceras) pueden enviar a mi API, '*'
     allow_headers=['accept', 'authorization']
     )

productos = [
    {
        'id': uuid4(),
        'nombre': 'Palta fuerte',
        'precio': 7.50,
        'disponibilidad': True
    },
    {
        'id': uuid4(),
        'nombre': 'Lechuga Carola',
        'precio': 1.50,
        'disponibilidad': True
    }
]

@app.route('/', methods = ['GET'])
def inicio():
    return {
        'message': 'Bienvenido a la API de Productos'
    }, 200

@app.route('/productos', methods = ['GET'])
def gestionProductos():
    return {
        'message': 'Los productos son',
        'content': productos
    }, 200

# Si voy a recibir un parametro dinamico (que va a cambiae su valor) y eso lo voy a manejar intenamente
# Los formatos que puedo parsear son:
# String > para recibir textos
# int > para recibir solo numeros
# float > para recubur numero con punto decimal
# path > que son string pero tambien aceptan slashes /
# uuid > aceptan UUID
# Al colocar un parseador si el formato que me envia el cliente no cumple con esta conversion no aceptara la peticion

@app.route('/producto/<uuid:id>', methods=['GET'])
def gestionProducto(id):
    print(id)
    # temenos una lista de productos en el cul cada posicion tenemos un diccionario y una llave llamada id
    # iteren esos productos y vean si existe el producto con determinado id
    # Si no existe entonces retornar un message que diga 'Producto no existe' con un estado 404
    # PISTA: hacer un for con if y else dentro de el

    for producto in productos:
        if producto['id'] == id:
            return {
                'content': producto
            }, 200

    return {
        'message': 'El producto no existe'
    }, 404

@app.route('/producto', methods=['POST'])
def crearProducto():
    # Convierte la data del body a un disccionario si el body es un JSON
    data = request.get_json() 
    # Antes de guardar la informacion en los productos agregarles el id
    data['id'] = uuid4()
    
    productos.append(data)
    return {
        'message': 'Producto creado exitosamente',
        'content': data
    }, 201 # created

if __name__ == '__main__':
    app.run(debug=True)