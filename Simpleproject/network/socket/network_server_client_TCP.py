import socket

HOST = "192.168.208.58"
PORT = 8000

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST,PORT))

    data = s.recv(1024)
    s.sendall("string").encode("ASCII")



