import socket
import threading
import sys

# Creamos un objeto socket:
client_socker = socket.socket()
# Establecemos la conexión (IP y puerto del servidor):
client_socker.connect(('localhost', 8000))

# Nombre del usuario:
print("")
nombre_del_cliente = input("Elige tu nombre para este servidor: ")
print("")
client_socker.send(nombre_del_cliente.encode())

# Lock para sincronizar el acceso a nombre_del_cliente
nombre_lock = threading.Lock()

# === HILO RECEPTOR: escucha todo lo que venga del servidor ===
def recibir_mensajes():
    global nombre_del_cliente
    while True:
        try:
            mensaje = client_socker.recv(1024).decode()
            
            if mensaje == "Mensaje recibido (visto por el servidor).":
                # Borra línea de input anterior y muestra solo "Visto"
                sys.stdout.write('\r\033[K')  # Borra línea actual
                sys.stdout.flush() # Para que el cursor de la consola aparezca inmediatamente. Borra de la memoria el mensaje anterior.
                print("Visto\n")
                print("Visto")
                print(f"{nombre_del_cliente}: ", end="", flush=True)
            
            else:
                sys.stdout.write('\r\033[K')
                sys.stdout.flush()
                print(mensaje)
                print()
                print(f"{nombre_del_cliente}: ", end="", flush=True)
        
        except:
            print("\nConexión cerrada por el servidor.")
            break  


# Lanzamos el hilo que escucha los mensajes entrantes
hilo_receptor = threading.Thread(target=recibir_mensajes, daemon=True)
hilo_receptor.start()

# === HILO PRINCIPAL: envía mensajes ===
print("Conectado al servidor. Escribe un mensaje (o '/exit' para salir):")

# Bucle infinito para enviar mensajes:
while True:
    with nombre_lock:
        mensaje = input(f"{nombre_del_cliente}: ")

    if mensaje.lower() == '/exit':
        print("Desconectando del servidor...")
        break

    elif mensaje.lower() == '/help':
        ayuda = """
Comandos disponibles:
/new_name_       -> Cambiar tu nombre
/users_          -> Ver usuarios conectados
/exit            -> Salir del servidor
"""
        print(ayuda)

    elif mensaje.lower() == '/new_name_':                     
        client_socker.send(mensaje.encode()) # Manda '/nombre_nuevo'.
        print(client_socker.recv(1024).decode())  # Mostrar "Elija su nombre nuevo..."
        cambio_de_nombre = input('')
        client_socker.send(cambio_de_nombre.encode())
        print(client_socker.recv(1024).decode())  # Mostrar confirmación
        nombre_del_cliente = cambio_de_nombre
    
    else:   
      # Enviamos el mensaje al servidor:
        client_socker.send(mensaje.encode())
        print("Enviado")  


# Cerramos la conexión
client_socker.close()