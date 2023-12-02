## Proyecto de Redes

Con este proyecto vas a poder crear una red privada usando el microcontrolador ESP32 para la transferencia de datos de un servirdor a un cliente.

Incluye 3 archivos:
  - AccessPoint.cpp
  - cliente.py
  - servidor.py

El archivo AccessPoint.cpp se encarga de la creación de la red privada. El ESP32 pasará a ser un Access Point el cual se encargará de asignar la ip a cada usuario conectado.

Datos de la Red:
  - IP Red: 192.168.5.0
  - IP Access Point: 192.168.5.1
  - Máscara Subred: 255.255.255.0
  - IP Disponibles: 254

El archivo servidor.py cargará un archivo PDF guardado en la carpeta en la que se encuentra guardado y lo distibuira a los clientes que lo soliciten.
El archivo cliente.py deberá ser ejecutado desde las computadoras que desean descargar el PDF que está alojado en la computadora del servidor.

DATOS IMPORTANTES:
La comunicación se realizará mediante el protocolo TCP/IP y usando sockets.
Se deberá declarar manualmente la IP del servidor desde cada cliente.
