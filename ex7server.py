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

    valor_produto = float(data)

    novo_valor = valor_produto * 1.25

    client_socket.send(str(novo_valor).encode())

client_socket.close()
server_socket.close()
