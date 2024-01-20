console.log('Hola')
const button = document.getElementById('crearProductoBtn')
const nombreProducto = document.getElementById('nombre')
const precioProducto = document.getElementById('precio')
const disponibleProducto = document.getElementById('disponible')

function crearProducto(e) {
    e.preventDefault()
    const body = {
        nombre : nombreProducto.value,
        precio: +precioProducto.value,
        disponible: disponibleProducto.checked
    }
    crearProductoRequest(body) //....
}

async function crearProductoRequest(body) {
    await fetch('http://127.0.0.1_5000/producto', {method: 'POST', body: JSON.stringify(body), header:{
        // Los headers sirven para enviar un encabezado de la peticion es decir gracias a estos el backend sabra que infomacion recibe, cuestiones de autenticacion, el origen de la peticion entre otros
        'Content-Type': 'application/json' // Indicar que lo que estamos enviando por eñl body es un JSON
    }})

    return solicitud.status === 200
}

button.addEventListener('click',crearProducto)

async function pedirProductos() {
    const solicitud = await fetch('http://127.0.0.1:5000/productos')

    console.log(solicitud.status)
    // O bien se usa el .text() o el .json() mas no se puede utilizar los dos a la vez
    // el text() se utiliza cuando el backend devuelve netamente texto 
    // const data = await solicitud.text() // es la informacion sin parsear (sin convertir a un formato legible en js)
    // cuando el backend devuelve diccionario 
    const data = await solicitud.json() // me da la informacion parseada para que JS la pueda entender
    console.log(data)
}

pedirProductos()