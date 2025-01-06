import socket

HOST = "26.168.209.82"
PORT = 8000

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST,PORT))

    while True:
        data = s.recv(1024)
        s.sendall("hello".encode("ASCII"))