import mouse
import socket

SX=2
SY=2


HOST = "192.168.208.58"
PORT = 8000
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    data_line = s.accept()[0]

SY=SY*1.5
def f(a,b,data):
    dx,dy=data.split()
    b+=int(dx)*SX*0.001
    a+=int(dy)*SY*0.001
    return a,b
rdata="0 0"
data="0 0"
x,y=1000,550
cpdata = " "
while True:
    rdata=str(data_line.recv(1024))[2:-1]
    if len(rdata.split())==2:
        data=rdata
        if cpdata != data:
            y, x = f(y, x, data)
        cpdata = data
    else:
        data="0 0"
    mouse.move(x,y)