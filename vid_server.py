import socket

HOST = socket.gethostbyname(socket.gethostname())
PORT = 6666

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))

server.listen(3)

while True:
    communication_socket, address = server.accept()
    print(f"Connected to: {address}")
