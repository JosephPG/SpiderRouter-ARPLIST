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

- Crear un handle para la cookie que contiene el usuario y contraseña en base64 

- Enviar la petición POST con la cookie 

- Obtener la data, convertir la IP(que esta representada como un entero), verificar si conocemos la mac, y dar
 un formato adecuado para imprimirlo.
