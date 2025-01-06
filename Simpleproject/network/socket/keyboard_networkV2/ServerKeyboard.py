import socket
import pygame
from pygame.locals import QUIT, KEYDOWN, KEYUP

# Initialize Pygame
pygame.init()

# Define the color white
WHITE = (255, 255, 255)
# Set the dimensions of the display window
X, Y = 800, 600
surface = pygame.display.set_mode((X, Y))


def start_server(HOST="192.168.1.39", PORT=8000):
    """
    Function to start the server and handle client connections and data exchange.
    """
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        try:
            s.bind((HOST, PORT))
            print(f"Server started on {HOST}:{PORT}")
        except OSError as e:
            if e.errno == 98:  # Error number 98: Address already in use
                print(f"Port {PORT} already in use, trying port {PORT + 1}")
                PORT += 1
                s.bind((HOST, PORT))
                print(f"Server started on {HOST}:{PORT}")
            else:
                print(f"Failed to start server on {HOST}:{PORT}: {e}")
                return
            
        running = True
        s.listen()
        print("Waiting for connections...")
        conn, addr = s.accept()
        print(f"Connected to {addr}")

        while running:
            pygame.time.Clock().tick(10)
            surface.fill(WHITE)
            pygame.display.flip()

            # Send the key pressed to the client
            for event in pygame.event.get():
                if event.type == QUIT:
                    running = False
                elif event.type == KEYDOWN:
                    print(event.unicode + "1")
                    conn.send((event.unicode + "1").encode())
                elif event.type == KEYUP:
                    print(event.unicode + "0")
                    conn.send((event.unicode + "0").encode())

if __name__ == '__main__':
    start_server()
