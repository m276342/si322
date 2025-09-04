#!/usr/bin/env python3

from socket import *

PORT = 1337

server_socket = socket(AF_INET, SOCK_STREAM)
server_socket.bind(("", PORT))
server_socket.listen(1)

print("[*] Server is listening...")

while True:
    connection_socket, address = server_socket.accept()
