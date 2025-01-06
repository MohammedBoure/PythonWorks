import socket
import pyaudio

def start_server(server_ip, server_port):
    p = pyaudio.PyAudio()
    stream = p.open(format=pyaudio.paInt16,
                    channels=2,
                    rate=44100,
                    input=True,
                    frames_per_buffer=1024)

    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as server_socket:
        try:
            server_socket.bind((server_ip, server_port))
            print(f"Server listening on {server_ip}:{server_port}")

            while True:
                data, client_address = server_socket.recvfrom(1024)
                print(f"Received data from {client_address}")
                stream.write(data)

        except Exception as e:
            print(f"Unexpected error: {e}")
        finally:
            stream.stop_stream()
            stream.close()
            p.terminate()

if __name__ == "__main__":
    server_ip = '192.168.1.39'
    server_port = 8000
    start_server(server_ip, server_port)
