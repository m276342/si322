#!/usr/bin/env python3

from socket import *

PORT = 8888

server_socket = socket(AF_INET, SOCK_STREAM)
server_socket.bind(("", PORT))
server_socket.listen(1)

print("[*] Server is listening...")

while True:
    connection_socket, address = server_socket.accept()
    sentence = connection_socket.recv(1024).decode()
    print(sentence)

    file_name = sentence.split(" ")[1][1:]
    content_type = "text/html"

    try:
        if file_name.endswith(".jpg"):
            f = open(file_name, "rb")
            content = f.read()
            content_type = "image/png"
        else:
            f = open(file_name or "index.html", "r")
            content = f.read().encode()
    except:
        f = open("index.html", "r")
        content = f.read().encode()

    f.close()

    HTTP_RESP = f"""HTTP/1.1 200 OK\r
Content-Length: {len(content)}\r
Content-Type: {content_type}\r
Connection: close\r
\r
""".encode() + content

    connection_socket.send(HTTP_RESP)
    connection_socket.close()

