import socket

def check_port(host, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(1)
    try:
        sock.connect((host, port))
    except socket.error:
        return False
    return True

hostname = '192.168.1.34'
port = 443

if check_port(hostname, port):
    print(f"Port {port} is open on {hostname}.")
else:
    print(f"Port {port} is not open on {hostname}.")
