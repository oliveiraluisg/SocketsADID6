import socket

HOST = '127.0.0.1'
PORT = 12121

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((HOST, PORT))

total_despesas = float(input("Insira o total de despesas do restaurante: "))

client_socket.send(str(total_despesas).encode())

total_com_gorjeta = client_socket.recv(1024)

print(f"O valor total com a gorjeta de 10% é: {total_com_gorjeta.decode()}")

client_socket.close()
