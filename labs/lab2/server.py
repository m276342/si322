#!/usr/bin/env python3

from socket import *

PORT = 1337

server_socket = socket(AF_INET, SOCK_STREAM)
server_socket.bind(("", PORT))
server_socket.listen(1)

print("[*] Server is listening...")

while True:
    connection_socket, address = server_socket.accept()
    sentence = connection_socket.recv(1024).decode("utf-8")
    capitilized_sentence = sentence.upper()
    connection_socket.send(capitilized_sentence.encode("utf-8"))
    connection_socket.close()

