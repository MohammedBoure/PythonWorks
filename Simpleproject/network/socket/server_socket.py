import socket

HOST = "26.168.209.82"
PORT = 8000

with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as s:
    try:
        s.bind((HOST,PORT))
        print("host:8000")
    except:
        print("host:8001")
        PORT = 8001
        s.bind((HOST, PORT))
    s.listen()
    data_line_1 = s.accept()[0]
    print("cnnecte player 1")

while True:
    data = data_line_1.recv(16).decode("ASCII")
    data = [data[i] for i in range(len(data))]
    for i in range(len(data)):
        list1.append(data[i])