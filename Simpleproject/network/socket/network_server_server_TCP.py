import socket

HOST = "192.168.105.219"
PORT = 8000

#listen and accept(create a data_line)
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    data_line , adrr = s.accept()

#data_line uses

with data_line:
    while 1:
        data = data_line.recv(1)
        print(data.decode("ASCII"))
