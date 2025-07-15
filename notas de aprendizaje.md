# Servidor:

Programa o computadora que proporciona servicios o recursos a otros programas o computadoras llamados clientes.

    En palabras simples:

    Un servidor "espera" conexiones y responde a peticiones.
    Un cliente se conecta al servidor para pedir algo.


# Cliente:

Un cliente es un programa o dispositivo que solicita servicios o recursos a un servidor a través de una red.

    En palabras simples:

    Un cliente pide algo, y el servidor responde.


# Socket:

Es una herramienta que permite establecer una conexión entre un servidor y uno o más clientes, permitiendo el intercambio de datos en tiempo real. Gracias a esta conexión, todos los clientes pueden recibir información actualizada del servidor, como mensajes nuevos, desconexiones de usuarios, cambios de estado, etc.

El cliente accede a este servicio del servidor a través de un puerto específico, y se identifica mediante su dirección IP, similar a una “cédula de identidad”, lo que permite reconocerlo dentro de la red.


# Analogía:

Proveedor...

Qué hace este proveedor? Manda producto, averigua si llegó y qué productos hay en el almacén.


Almacén:

Guarda, enseña y dice que producto tiene...


Producto:

Lo que se envía y se muestra.


Barco (tipo tal de barco):

El que transporta el producto.


Puerto (ya asignado al almacén):

Todos los barcos de "tal tipo, van a llegar pa cá"


Proveedor = Cliente
Almacén = Servidor
Producto = Servicio (el mensaje del cliente)
Barco = Socket
Puerto = El puerto: el número específico donde el servidor escucha (ej: 80, 443). La parte del servidor a la que el mensaje llegará.