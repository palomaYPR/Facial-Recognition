
# Class that contains the client, that will send the photograph to the server to later verify if it contains a face

import socket

# Definimos parámetros necesarios por defecto
ip = 'localhost'
puerto = 9797
dataConection = (ip, puerto)
conexionesMax = 5  # Podrán conectarse 5 

# Creamos el servidor
# socket.AF_INET para indicar que utilizaremos Ipv4
# socket.SOCK_STREAM para utilizar TCP/IP (no UDP)
socketServidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

socketServidor.bind(dataConection) # Asignamos los valores del servidor
socketServidor.listen(conexionesMax) # Asignamos el número máximo de conexiones

print('Esperando conexiones en %s:%s' %(ip,puerto))
client, direccion = socketServidor.accept()
print('Conexión establecida con %s:%s' %(direccion[0],direccion[1]))

#Bucle de escucha. En él indicamos la forma de actuar al recibir las tramas
while True:
    msg = '1.jpg' 
    client.send(msg.encode())
    data = client.recv(1024)
    if not data:
        print('-- NO FACE --')
        break
    else:
        print(data)
        break
print('\n---------- CONEXIÓN CERRADA ----------')
socketServidor.close()
