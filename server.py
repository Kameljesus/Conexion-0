# Importamos la librería socket.
import socket
import threading

# Lista de clientes en el servidor (se pone como una variante global, ya que va a funcionar para todos los clientes):
lista_de_clientes = []
lock = threading.Lock() 

# Creamos mi socket (mi conexión):
mi_socket = socket.socket()

# Establecemos nuestra conexión:
# Establezco la IP y el puerto para mi socket
mi_socket.bind(('localhost', 8000))

# Establecemos la cantidad de conexiones que puede manejar mi socket en cola:
mi_socket.listen(5)

# Esta función se ejecutará en un hilo diferente para cada cliente:
def manejar_cliente(conexion, addr):
    nombre_del_cliente = conexion.recv(1024).decode()
    with lock:
        lista_de_clientes.append(nombre_del_cliente)

    print(f"{nombre_del_cliente} conectado desde {addr}")


    while True:
        try:
            # Recibimos la petición del cliente
            mensaje = conexion.recv(1024).decode() # .decode() se refiere a "descodificar", que es el pasar el código de bytes (binario) de la computadora a string.
            
            # El cliente se desconectó:
            if not mensaje:
                break

            elif mensaje == '/usuarios':
                conexion.send(f"{lista_de_clientes}".encode())
            
            elif mensaje == '/nombre_nuevo':
                lista_de_clientes.pop(nombre_del_cliente)
                conexion.send("Elija su nombre nuevo para este servidor:".encode())
                nombre_del_cliente = conexion.recv(1024).decode()
            
            else:
                print(f"[{nombre_del_cliente}] dijo: {mensaje}")
                # Cuando el cliente se conecte al solicitar, le mandaremos este mensaje:
                # Se pueden enviar mensajes, archivos, imágenes, mp3, etc.
                conexion.send(f"{mensaje}".encode()) # .encode() se refiere a "codificar", es pasar el string a bytes (binario), ya que la computadora lo lee de esa forma.
        
        
        except Exception as e:
            print(f"Error con el cliente {addr}: {e}")
            # print(f"Error con el cliente {addr}: {e}")
            # Muestra un mensaje de error en la consola para que sepas qué falló y con qué cliente. Por ejemplo:
            # Error con el cliente ('127.0.0.1', 53222): [Errno 104] Connection reset by peer
            break
            # Corta el while True: de ese cliente, porque ya no tiene sentido seguir intentando leer o enviar si hubo un fallo.

        '''
        except Exception as e:
        
        Captura cualquier error o excepción que ocurra dentro del bloque try, por ejemplo:

            - El cliente cerró su ventana de forma brusca.

            - Se perdió la conexión.

            - Se mandaron datos corruptos.

            - O cualquier otro error imprevisto
        
        En vez de hacer simplemente except: (lo cual es muy genérico y oculta errores importantes), esta forma captura cualquier excepción y te la guarda en la variable e.
        '''


    print(f"{nombre_del_cliente} se desconectó.")
    conexion.close()

'''
manejar_cliente(...): función que maneja a un cliente en un hilo separado.

Cada vez que un cliente se conecta, se crea un nuevo hilo con Thread(...).

Así el servidor puede seguir aceptando más clientes mientras ya está hablando con otros.
'''

while True:
    '''
    Conexion: Es el objeto socket que se usa para comunicarte con ese cliente específico. 

    addr: es una tupla que contiene:

        la IP del cliente (por ejemplo, '127.0.0.1')
        el puerto desde donde el cliente se conectó (por ejemplo, 53722)
    '''
    # Con esta linea aceptamos las peticiones del cliente:
    conexion, addr = mi_socket.accept()
    print("")
    print("Nueva conexión establecida!")
    print("")

    # Crea un hilo para cada nuevo cliente
    hilo = threading.Thread(target=manejar_cliente, args=(conexion, addr))
    hilo.start()