# Spider for Router

Spider hecho especificamente para el Firmware router TP-LINK TD-W8970.

## Procesos

- ##### Login:

 El proceso de ingreso crea una cookie con el usuario y contraseña convertido en base64, esta es enviada en
 cada petición al servidor y validada por este.

- ##### Obtención de lista ARP:

 Se realiza petición POST al cual se envía una cadena indicando el formato en el que se recibirá la data, esta
 es una cadena que contiene la lista ARP.

## Desarrollo

- Crear un handle para la cookie que contiene el usuario y contraseña en base64. 

- Enviar la petición POST con la cookie. 

- Obtener la data, convertir la IP(que esta representada como un entero), verificar si la mac es conocido, y dar
 un formato adecuado para imprimir.

![router](https://user-images.githubusercontent.com/25994826/37258509-25688b68-2547-11e8-87d3-a79b2a5d1e3d.jpeg)
![console](https://user-images.githubusercontent.com/25994826/37258508-222ce520-2547-11e8-90c3-9f4eae2e6176.jpeg)
