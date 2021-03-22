import socket
import time
import sys
import argparse


# argv = sys.argv[1:]

def print_socket_attr(sock: socket.socket) -> None:
    print(f"socket family: { sock.family }")
    print(f"socket type: {sock.type}")
    print(f"socket protocol: {sock.proto}")

def get_RFC868_time_protocol_timestamp() -> int:
    """ Returns the time in seconds since midnight on January first 1900 as a 32 bit integer.
        Implements the Time Protocol as described in RFC860.
        https://tools.ietf.org/html/rfc868
    """
    NUMBER_OF_SECONDS_FROM_JANUARY_FIRST_1900_TO_BEGINNING_OF_UNIX_EPOCH: int = 2208988800
    time_since_beginning_of_unix_epoch: int = int(time.time())
    return NUMBER_OF_SECONDS_FROM_JANUARY_FIRST_1900_TO_BEGINNING_OF_UNIX_EPOCH + time_since_beginning_of_unix_epoch


parser = argparse.ArgumentParser()

parser.add_argument(
    "-H",
    "--host",
    type=str,
    default="127.0.0.1",
    help="The server host address. Must be IPV4"
)

parser.add_argument(
    "-p",
    "--port",
    type=int,
    default=20000,
    help= "server port number"
)
# parser.add_argument(dest = 'host-address', type = str, help = "The server host address. Must be IPV4")
# parser.add_argument(dest = 'port', type = int, help "server port number")

args = parser.parse_args()

HOST: str = args.host
PORT: int = args.port



# create a BSD socket, which uses TCP/IP for communication
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM, socket.getprotobyname('tcp'))

sock.bind((HOST, PORT))

print_socket_attr(sock)

MAXIMUM_NUMBER_OF_ALLOWED_QUEABLE_CONNECTIONS: int = 5
sock.listen(MAXIMUM_NUMBER_OF_ALLOWED_QUEABLE_CONNECTIONS)

while True:
    connection, addr = sock.accept()
    connection.send(bytes(get_RFC868_time_protocol_timestamp()))
    connection.close()


# if __name__ == '__main__':
#     main()






# try:
#     sock.close()
# except OSError:
#     pass


