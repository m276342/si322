#!/usr/bin/env python3

# Title:        foo.py
# Description:  foo
# Author:       bluecosmo

import socket

HOST = '127.0.0.1'  # Standard loopback interface address (localhost)
PORT = 8000         # Port to listen on (non-privileged ports are > 1023)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    print(f"Listening on port {PORT}...")
    conn, addr = s.accept()
    with conn:
        print(f"Connected by {addr}")
        data = conn.recv(1024)  # Receive up to 1024 bytes
        print(f"Received: {data.decode()}")

        # Simple HTTP response
        response = b"HTTP/1.1 200 OK\r\nContent-Type: text/html\r\n\r\n<h1>Hello from Python Socket Server!</h1>"
        conn.sendall(response)
