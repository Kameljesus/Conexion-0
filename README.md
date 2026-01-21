# Conexion-0

Proyecto educativo de **comunicación cliente-servidor** implementado en Python utilizando **sockets TCP** y **multithreading**.  
Permite que múltiples clientes se conecten a un servidor central y se envíen mensajes en tiempo real, simulando un chat básico por consola.

El objetivo principal del proyecto es comprender cómo funcionan las conexiones de red, el manejo de múltiples clientes y la comunicación concurrente.

---

## 🧠 Descripción general

El sistema está compuesto por dos programas:

- **Servidor (`server.py`)**
  - Escucha conexiones entrantes en un host y puerto específicos.
  - Acepta múltiples clientes simultáneamente.
  - Reenvía los mensajes recibidos a todos los clientes conectados (excepto al emisor).
  - Maneja desconexiones normales y abruptas.

- **Cliente (`client.py`)**
  - Se conecta al servidor mediante sockets.
  - Permite al usuario elegir un nombre.
  - Envía mensajes al servidor desde la consola.
  - Recibe mensajes en tiempo real usando un hilo independiente.

---

## ⚙️ Funcionalidades principales

- Conexión cliente-servidor mediante **sockets TCP**
- Manejo de múltiples clientes con **threads**
- Comunicación bidireccional en tiempo real
- Confirmación de mensajes enviados
- Manejo de errores y desconexiones
- Comando `/exit` para salir de forma controlada

---

## 🛠️ Tecnologías utilizadas

- **Python 3**
- **socket** (comunicación en red)
- **threading** (concurrencia)
- **sys** (manejo de salidas del programa)
- Codificación **UTF-8**

---

## 📂 Estructura del proyecto

Conexion-0/
│
├── server.py # Servidor que maneja múltiples clientes
├── client.py # Cliente que se conecta y envía mensajes
└── notas_de_aprendizaje.md # Apuntes y conceptos teóricos del proyecto

---

## ▶️ Cómo ejecutar el proyecto

### Requisitos
- Python 3 instalado

### Pasos

1. Clonar el repositorio:
   ```bash
   git clone https://github.com/Kameljesus/Conexion-0.git
   
2. Iniciar el servidor:
  python server.py

3. En otra terminal, iniciar uno o más clientes:
  python client.py

4. Escribir mensajes desde cada cliente para ver la comunicación en tiempo real.
