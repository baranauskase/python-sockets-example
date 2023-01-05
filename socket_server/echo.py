import socket
from socket_server.config import DEFAULT_HOST, DEFAULT_PORT


def start_server(host=DEFAULT_HOST, port=DEFAULT_PORT):
    # Creates a TCP socket object using IPv4 address family
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:

        # Associate the socket with the host address and port
        # Note that using host name instead of IP has undeterministic behaviour
        # since Python will perform a DNS lookup and use the first IP address.
        s.bind((host, port))

        # Start listening for incoming connections using default backlog size
        s.listen()

        # Wait for new connections. Once connection is established with a client
        # we get a new connection socket that is different from the listening socket
        # and a client address.
        conn, addr = s.accept()
        with conn:
            print(f"Connected by {addr}")
            # Infinite loop to receive all data from the client and send it back
            # Once we encounter empty bytes we can break the loop.
            while True:
                data = conn.recv(1024)
                if not data:
                    break
                conn.sendall(data)
