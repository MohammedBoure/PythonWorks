import socket
import keyboard

def main():
    """
    Function to read keyboard events and return the name of the key pressed.
    """
    print("Press ESC to exit.")
    while True:
        try:
            event = keyboard.read_event()
            if event.event_type == keyboard.KEY_DOWN:
                if event.name == "esc":
                    print("Exiting...")
                    return "exit"
                else:
                    print(f"Key pressed: {event.name}")
                    return event.name
        except Exception as e:
            print(f"Error: {e}")

def start_server(HOST="192.168.1.36", PORT=8000):
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
        
        s.listen()
        print("Waiting for connections...")
        conn, addr = s.accept()
        print(f"Connected to {addr}")

        while True:
            try:
                key_pressed = main()  # Call main() function to get the key pressed
                if key_pressed == "exit":
                    break
                
                # Send the key pressed to the client
                conn.send(key_pressed.encode())


            except Exception as e:
                print(f"Error: {e}")
                break

if __name__ == '__main__':
    start_server()
