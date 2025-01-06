import socket
import keyboard
from time import sleep

def press_key(text):
    if text[1]=="1":
        keyboard.press(text[0])
    elif text[1]=="0":
        try:keyboard.release(text[0])
        except:pass

def filter_text(text):  #><
    i = 0
    list_text = []
    while i < len(text):
        list_text.append((text[i]+text[i+1]))
        i += 2
    for i in list_text:
        press_key(i)

def main_press(text):
    if len(text)>2:
        filter_text(text)
    elif len(text)== 2:
        press_key(text)

def client_program():
    host = "192.168.1.36"
    port = 8000
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        try:
            s.connect((host, port))
            print("Connected to server on port", port)
        except ConnectionRefusedError:
            # If connection fails on port, try connecting to port + 1
            port += 1
            s.connect((host, port))
            print("Connected to server on port", port)

        while True:
            data = s.recv(1024).decode()  # Receive data from server
            print(data)
            main_press(data)

try:
    if __name__ == '__main__':
        client_program()
except:pass
