import socket
import keyboard
from time import sleep
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

            
            try:
                print(data)
                keyboard.press(data)  # Press the key received from server
                sleep(0.1)
                keyboard.release(data)

            except Exception as e:
                print("Failed to press key:", e)


if __name__ == '__main__':
    client_program()

