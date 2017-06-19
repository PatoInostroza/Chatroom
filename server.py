import socket

socket = socket.socket()
socket.bind(("192.168.0.10", 44000))
socket.listen(1)

print("Esperando conexion")
cliente, addr = socket.accept()
print("Conexion establecida")

while True:
    print("...")
    recibido = cliente.recv(128)
    mensaje = recibido.decode('utf-8')
    if mensaje == "Adios":
        break
    print(addr, "Dice: ", mensaje)

print("Adios Mundo")

cliente.close()
socket.close()
mensaje = input("Enter key to End:")
