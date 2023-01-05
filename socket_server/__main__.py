import argparse
from enum import Enum
import socket_server.echo as echo


class Server(Enum):
    echo = "echo"
    multi = "multi"

    def __str__(self):
        return self.value


parser = argparse.ArgumentParser(description="Start socket server.")
parser.add_argument(
    "server", type=Server, choices=list(Server), help="Socket server type"
)

args = parser.parse_args()
if args.server == Server.echo:
    echo.start_server()
