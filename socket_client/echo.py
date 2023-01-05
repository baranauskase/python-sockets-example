import socket
from socket_client.config import DEFAULT_HOST, DEFAULT_PORT


def start_client(host=DEFAULT_HOST, port=DEFAULT_PORT):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((host, port))
        s.sendall(b"Hello, world")
        data = s.recv(1024)

    print(f"Received {data!r}")
