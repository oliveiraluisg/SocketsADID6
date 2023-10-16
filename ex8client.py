import socket

HOST = '127.0.0.1'
PORT = 12121

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((HOST, PORT))

peso_atual = float(input("Insira o peso atual: "))
peso_desejado = float(input("Insira o peso desejado: "))

client_socket.send(f"{peso_atual},{peso_desejado}".encode())

percentual_eliminar = client_socket.recv(1024)

print(f"O percentual de peso a ser eliminado é: {percentual_eliminar.decode()}%")

client_socket.close()