# Importamos la librería socket.
import socket
import threading
import sys

print("")

# Creamos mi socket (mi conexión):
server_socket = socket.socket()

# Establecemos nuestra conexión:
# Establezco la IP y el puerto para mi socket
server_socket.bind(('localhost', 8000))

# Establecemos la cantidad de conexiones que puede manejar mi socket en cola:
server_socket.listen(5)

# Lista de clientes en el servidor (se pone como una variante global, ya que va a funcionar para todos los clientes):
lista_de_clientes = []
lista_de_conexiones = []
lock = threading.Lock() # También necesitás usar un lock (candado) para que no haya conflictos entre hilos.

# Esta función se ejecutará en un hilo diferente para cada cliente:
def manejar_cliente(conexion, addr):
    global lista_de_clientes # Para modificarla
    nombre_del_cliente = None # Declaracion segura.
    
    try:
        nombre_del_cliente = conexion.recv(1024).decode()
        
        with lock:
            lista_de_clientes.append(nombre_del_cliente)

        print(f"{nombre_del_cliente} se ha conectado desde {addr}")

        while True:

                # Recibimos la petición del cliente
                mensaje = conexion.recv(1024).decode() # .decode() se refiere a "descodificar", que es el pasar el código de bytes (binario) de la computadora a string.
                
                # El cliente se desconectó:
                if not mensaje:
                    break

                elif mensaje == '/users_':
                    with lock:
                        lista = "\n".join(lista_de_clientes)  # Une los nombres con saltos de línea
                        conexion.send(lista.encode()) # "Pepito\nJuan\nLucía". Es lo que se mandará como un solo string codificado, y el cliente lo verá de forma vertical.
                
                elif mensaje == '/new_name_':                             
                    conexion.send("Elija su nombre nuevo para este servidor:".encode())
                    nuevo_nombre = conexion.recv(1024).decode()

                    with lock:
                        if nombre_del_cliente in lista_de_clientes:
                            index = lista_de_clientes.index(nombre_del_cliente) # index() busca la posición del primer elemento que coincida. Si no lo encuentra, lanza un error: ValueError.
                            lista_de_clientes[index] = nuevo_nombre            
                    
                    conexion.send(f"Tu nombre fue cambiado de '{nombre_del_cliente}' a '{nuevo_nombre}'.".encode())
                    print(f"{nombre_del_cliente} cambió su nombre a {nuevo_nombre}")
                    nombre_del_cliente = nuevo_nombre
             
                else:
                    mensaje_formateado = f"[{nombre_del_cliente}]: {mensaje}"

                    # Confirmación al remitente:
                    try:
                        conexion.send("Mensaje recibido (visto por el servidor).".encode())
                    except:
                        pass

                    print(mensaje_formateado)

                    # Enviamos el mensaje a todos los demás clientes conectados
                    with lock:
                        for conn in lista_de_conexiones:
                            try:
                                if conn != conexion:  # Opcional: no te lo mandes a ti mismo
                                    conn.send(mensaje_formateado.encode())
                            except:
                                pass  # Si falla un cliente, lo ignoramos por ahora
            
        
    except Exception as e:
            print(f"Error con el cliente {addr}: {e}")
            # print(f"Error con el cliente {addr}: {e}")
            # Muestra un mensaje de error en la consola para que sepas qué falló y con qué cliente. Por ejemplo:
            # Error con el cliente ('127.0.0.1', 53222): [Errno 104] Connection reset by peer.

            """
            Captura cualquier error:
            - El cliente cerró su ventana de forma brusca.
            - Se perdió la conexión.
            - Se mandaron datos corruptos.
            """
    
    finally:
        # Cliente se desconectó
        with lock:
            if nombre_del_cliente in lista_de_clientes:
                lista_de_clientes.remove(nombre_del_cliente)
            if conexion in lista_de_conexiones:
                lista_de_conexiones.remove(conexion)
        print("")
        print(f"{nombre_del_cliente} se desconectó.")
        print("")
        conexion.close()

        # Si no queda ningún cliente conectado, cerramos el servidor
        with lock:
            if not lista_de_clientes:
                print("Todos los clientes se desconectaron. Cerrando el servidor.")
                server_socket.close()
                sys.exit(0)  # Salimos del programa completamente

'''
manejar_cliente(...): función que maneja a un cliente en un hilo separado.

Cada vez que un cliente se conecta, se crea un nuevo hilo con Thread(...).

Así el servidor puede seguir aceptando más clientes mientras ya está hablando con otros.
'''

while True:
    try:
        '''
        Conexion: Es el objeto socket que se usa para comunicarte con ese cliente específico. 

        addr: es una tupla que contiene:

            la IP del cliente (por ejemplo, '127.0.0.1')
            el puerto desde donde el cliente se conectó (por ejemplo, 53722)
        '''
        # Con esta linea aceptamos las peticiones del cliente:
        conexion, addr = server_socket.accept()
        with lock:
            lista_de_conexiones.append(conexion)
        print("Nueva conexión establecida!")
        print("")
        
        # Crea un hilo para cada nuevo cliente
        hilo = threading.Thread(target=manejar_cliente, args=(conexion, addr))
        hilo.start()
    
    except OSError:
        # Esto se activa si el socket fue cerrado desde `sys.exit()`
        break