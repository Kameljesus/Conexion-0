import socket

# Creamos un objeto socket:
mi_socket = socket.socket()

# Establecemos la conexión (IP y puerto del servidor):
mi_socket.connect(('localhost', 8000))

print("")
print("Conectado al servidor. Escribe un mensaje (o 'salir' para desconectar):")
print("")
nombre_del_cliente = input("Elige tu nombre para este servidor: ")
mi_socket.send(nombre_del_cliente.encode())

# Bucle infinito para enviar mensajes:
while True:
    mensaje = input(f"{nombre_del_cliente}: ")
    print("")

    if mensaje.lower() == '/salir':
        print("Desconectando del servidor...")
        break

    elif mensaje.lower() == '/nombre_nuevo':
        mi_socket.send(mensaje.encode())
        mi_socket.recv(1024).decode()
        cambio_de_nombre = input('')
        mi_socket.send(cambio_de_nombre.encode())
        nombre_del_cliente = cambio_de_nombre

    else:   
        # Enviamos el mensaje al servidor:
        mi_socket.send(mensaje.encode())

        # Esperamos la respuesta del servidor:
        respuesta = mi_socket.recv(1024).decode()
        print(f"El servidor ha recibido: {respuesta}")
        print("")

# Cerramos la conexión
mi_socket.close()