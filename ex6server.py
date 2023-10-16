import socket

HOST = '127.0.0.1'
PORT = 12121

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))
server_socket.listen(1)

print("Aguardando conexão do cliente...")

client_socket, addr = server_socket.accept()
print(f"Conexão estabelecida com {addr}")

while True:
    data = client_socket.recv(1024)
    if not data:
        break

    total_despesas = float(data)

    gorjeta = total_despesas * 0.10

    total_com_gorjeta = total_despesas + gorjeta

    client_socket.send(str(total_com_gorjeta).encode())

client_socket.close()
server_socket.close()
