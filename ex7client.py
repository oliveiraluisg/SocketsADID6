import socket

HOST = '127.0.0.1'
PORT = 12121

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((HOST, PORT))

valor_produto = float(input("Insira o valor do produto: "))

client_socket.send(str(valor_produto).encode())

novo_valor = client_socket.recv(1024)

print(f"Novo valor de venda com um aumento de 25%: {novo_valor.decode()}")

client_socket.close()
