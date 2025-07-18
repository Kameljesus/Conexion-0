## Servidor:

Programa o computadora que proporciona servicios o recursos a otros programas o computadoras llamados clientes.

    En palabras simples:

    Un servidor "espera" conexiones y responde a peticiones.
    Un cliente se conecta al servidor para pedir algo.


## Cliente:

Un cliente es un programa o dispositivo que solicita servicios o recursos a un servidor a través de una red.

    En palabras simples:

    Un cliente pide algo, y el servidor responde.


## Socket:

Es una herramienta que permite establecer una conexión entre un servidor y uno o más clientes, permitiendo el intercambio de datos en tiempo real. Gracias a esta conexión, todos los clientes pueden recibir información actualizada del servidor, como mensajes nuevos, desconexiones de usuarios, cambios de estado, etc.

El cliente accede a este servicio del servidor a través de un puerto específico, y se identifica mediante su dirección IP, similar a una “cédula de identidad”, lo que permite reconocerlo dentro de la red.


## Analogía:

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
Producto = Servicio (el mensaje del cliente).
Barco = Socket
Puerto = El puerto: el número específico donde el servidor escucha (ej: 80, 443). La parte del servidor a la que el mensaje llegará.


## Thread (hilo):

Es como un subproceso dentro de un programa, que permite que tu código haga varias cosas al mismo tiempo (o al menos, que lo parezca).

En la práctica:

Normalmente, tu programa en Python hace una cosa a la vez:

    1. Espera input

    2. Ejecuta algo

    3. Espera la siguiente cosa...

Pero si querés que el servidor maneje a varios clientes al mismo tiempo, no podés permitir que se quede esperando a que un solo cliente termine de hablar.

Ahí es donde entran los Threads.


# Analogía:

🔌 Socket = el cable físico principal que conecta tu computadora con el servidor (como si fuera un cable de red virtual).

🧵 Hilos (threads) = los cables de cobre dentro del socket, cada uno especializado:

    - Uno manda datos (como tus mensajes).

    - Otro recibe datos (mensajes del servidor).

    - Otros podrían hacer cosas como controlar comandos o manejar archivos, si quisieras.

🧠 Memoria compartida del programa = una caja de control central donde todos esos hilos leen y escriben información. Esto incluye:

    - El nombre del usuario

    - Los mensajes que llegan o se envían

    - El estado de conexión

    - Comandos pendientes (como /users_)

⏱️ Y como están todos conectados a la misma memoria, deben tener cuidado de no pisarse entre sí (por eso usamos lock, como un semáforo que dice quién puede tocar qué en qué momento).


# ¿Por qué decimos "parece"?

Porque en realidad:

    Python (por dentro) no ejecuta múltiples líneas exactamente al mismo tiempo, a menos que uses procesos o múltiples núcleos.

    Pero lo que hace Thread es intercalar rápidamente las instrucciones de cada hilo. Tan rápido que parece que todo pasa al mismo tiempo.

💡 Para tí como programador, sí: puedes escribir código que responde a varios eventos al mismo tiempo, como:

    recibir mensajes de 5 clientes distintos,

    imprimir cosas mientras escuchás conexiones,

    enviar mensajes sin bloquear nada.


## Host:

Un host (anfitrión en inglés) es cualquier dispositivo conectado a una red que:

    - Tiene una dirección IP

    - Puede enviar o recibir datos

Es decir, un host es una computadora, teléfono, servidor, router, impresora, etc. que participa en la red.


# ¿Qué hace un host?

Un host puede:

    - Conectarse a otros hosts (por IP)

    - Enviar/recibir mensajes

    - Ejecutar servidores o clientes

    - Participar en protocolos de red como HTTP, FTP, DNS, etc.


# ¿Un host es lo mismo que un servidor?

    - No exactamente.

    - Un servidor es un tipo de host que espera conexiones y responde peticiones.

    - Un cliente es otro host que inicia la conexión.

En tu chat por sockets:

    - El servidor es un host que espera conexiones.

    - Cada cliente es otro host que se conecta.


# ¿Y qué es el hostname?

El hostname es simplemente el nombre del host. Ejemplos:

    - En Linux: mi-laptop.local

    - En red: servidor-web.local

    - En internet: google.com (que se traduce a una IP)


# ¿Por qué la conexión muestra 6 números en la IP?
El valor de addr es una tupla que contiene:
('127.0.0.1', 56789)

No son 6 números, sino:

    4 números para la IP (IPv4): 192.168.0.103

    1 número adicional que es el puerto (entre 1024 y 65535): 50124

¿Y por qué ese puerto cambia?

Porque es un puerto efímero (temporal) que el sistema operativo le asigna automáticamente al cliente para conectarse. Cada cliente usa un puerto diferente, incluso si se conecta desde la misma máquina.


## ¿Qué es IPv4?:

IPv4 significa "Internet Protocol version 4", o sea, Protocolo de Internet versión 4. Es el sistema más común para identificar dispositivos en una red, como computadoras, teléfonos, routers, etc.


¿Cómo se ve una dirección IPv4?

Una dirección IPv4 está compuesta por 4 números separados por puntos. Ejemplos:

    - 192.168.0.1

    - 10.0.0.8

    - 127.0.0.1 (esta es la dirección local, llamada localhost)

Cada número va del 0 al 255 (porque usa 8 bits por número → 4 × 8 = 32 bits).


# Mejor explicacion:

¿Por qué tiene 4 números?

IPv4 (Internet Protocol versión 4) es un sistema de direcciones de 32 bits. Estos 32 bits se dividen en 4 bloques de 8 bits (un byte), y cada bloque se representa como un número del 0 al 255.

Por ejemplo:

192.168.1.5

    192 → 8 bits

    168 → 8 bits

    1 → 8 bits

    5 → 8 bits

Total: 8 × 4 = 32 bits


# ¿Qué hace IPv4?

IPv4 es como el sistema postal de Internet. Su trabajo es:

    - Darle a cada dispositivo una dirección única

    - Permitir que los datos lleguen desde un origen hasta un destino a través de redes

    - Fragmentar y enrutar los paquetes de datos correctamente


# ¿Qué hace cada número?

Los 4 números no tienen un significado fijo por sí solos, pero en general:
🔹 Se dividen en 2 partes:

    Red (Network)

    Host (Dispositivos dentro de la red)

La división depende de algo llamado máscara de subred (como 255.255.255.0), pero aquí va una idea general:
Parte	Ejemplo	Significado
Red	192.168.1	Identifica una red local
Host	5	Identifica un dispositivo dentro de esa red

Ejemplo:

Red: 192.168.1.0
Host 1: 192.168.1.5
Host 2: 192.168.1.6


# ¿Por qué del 0 al 255?

Porque cada número representa 8 bits, y con 8 bits podés representar 256 valores (de 0 a 255):

11111111 = 255 (en binario)
00000000 = 0


# Ejemplo visual (simplificado):

Supongamos esta IP:

192.168.1.10

Se ve así en binario:

192   = 11000000  
168   = 10101000  
1     = 00000001  
10    = 00001010

En total son 32 bits:
11000000.10101000.00000001.00001010


## Puerto:


# ¿Qué es un puerto en sockets?

Un puerto es un número (entre 0 y 65535) que identifica una aplicación o servicio específico que está usando tu red.

Tu computadora puede tener muchos servicios en red funcionando al mismo tiempo, y cada uno usa un puerto distinto para que no se confundan.


# Rango de puertos: ¿qué significan?

| Rango             | Nombre                                            | Uso                                                                                      |
| ----------------- | ------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| **0 - 1023**      | **Puertos "bien conocidos"** (*well-known ports*) | Reservados para servicios del sistema como HTTP, FTP, SSH, DNS, etc.                     |
| **1024 - 49151**  | **Puertos registrados** (*registered ports*)      | Se usan para programas de usuario o servidores específicos que necesitan un puerto fijo. |
| **49152 - 65535** | **Puertos dinámicos/efímeros**                    | Usados temporalmente por el sistema para conexiones salientes o pruebas.                 |


# ¿Por qué NO usas puertos 0–1023 normalmente?

Porque:

    - Son reservados por el sistema operativo (root o administrador).

    - No se recomienda usarlos para tus propios servidores o pruebas.

    - Usarlos puede generar conflictos con servicios ya instalados (por ejemplo, el puerto 80 lo usa HTTP).


# ¿Por qué usas puertos entre 1024 y 65535?

Porque:

    Están libres para ti como programador.

    No necesitas permisos especiales.

    Son seguros para pruebas de red y desarrollo de sockets.


## Que es "utf-8":

UTF-8 es un formato de codificación que convierte texto (letras, símbolos, emojis, etc.) a bytes y viceversa.
Los sockets solo pueden enviar/recibir bytes, pero vos trabajás con texto. Entonces necesitás traducir entre ambos.


# ¿Qué pasa si no especificás "utf-8"?

En la mayoría de los casos, Python usa "utf-8" por defecto, así que esto funciona igual:

mensaje.encode()      # lo codifica en utf-8
mensaje.decode()      # lo decodifica en utf-8


# ¿Por qué es importante usar UTF-8?

    Porque es compatible con casi todos los idiomas y emojis.

    Porque evita errores como:
    UnicodeDecodeError: 'ascii' codec can't decode byte ...

    Porque asegura que todos los caracteres especiales (ñ, á, ö, €, ❤️) se transmitan bien.


## Que es AF_INET?

    - AF = Address Family (Familia de Direcciones)

    - INET = Internet (IPv4)

Entonces, AF_INET significa: "Estoy usando direcciones IPv4", es decir, direcciones del tipo:

192.168.1.5
127.0.0.1
8.8.8.8


# ¿Dónde se usa?

Cuando creás un socket:

import socket

socket.socket(socket.AF_INET, socket.SOCK_STREAM)

Esto le dice al sistema:

    AF_INET: voy a usar IPv4.

    SOCK_STREAM: quiero una conexión tipo TCP (flujo de datos confiable, como en los chats).


# Otros valores posibles:

| Constante  | Significa                           | Uso común                            |
| ---------- | ----------------------------------- | ------------------------------------ |
| `AF_INET`  | IPv4                                | El más usado                         |
| `AF_INET6` | IPv6                                | Para direcciones como `2001:0db8::1` |
| `AF_UNIX`  | Sockets locales (solo en Linux/mac) | Comunicación entre procesos          |


# Ejemplo real:

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("localhost", 8000))

→ Le estás diciendo: "Conectame a una dirección IPv4, usando protocolo TCP".