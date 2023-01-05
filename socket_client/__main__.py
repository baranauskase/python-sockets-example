import argparse
from enum import Enum
import socket_client.echo as echo


class Client(Enum):
    echo = "echo"

    def __str__(self):
        return self.value


parser = argparse.ArgumentParser(description="Start client.")
parser.add_argument("client", type=Client, choices=list(Client), help="Client type")

args = parser.parse_args()
if args.client == Client.echo:
    echo.start_client()
