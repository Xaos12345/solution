#!/usr/bin/env python3

import socket
g = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
g.connect(("gmail.com",80))#Check ip in google
print(g.getsockname()[0])
ssdd = g.getsockname()[0]
g.close()
HOST = '0.0.0.0'  # Standard loopback interface address (localhost)
PORT = 65432        # Port to listen on (non-privileged ports are > 1023)
#sss
print(HOST)
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()
    with conn:
        print('Connected by', addr)
        while True:
            data = conn.recv(1024)
            if not data:
                break
            conn.sendall(data)
