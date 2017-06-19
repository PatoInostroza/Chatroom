import socket

socket = socket.socket()
print("Intentando conectar a Servidor...")
while True:
        socket.connect(("192.168.0.10", 44000))
        break

print("Conexion establecida")

while True:
      mensaje = input("Escribe tu mensaje: ")
      paquete = mensaje.encode('utf-8')
      if mensaje == "Adios":
      	socket.send(paquete)
      	break
      socket.send(paquete)

s.close()
print("Adios Mundo")