import socket
import sys

sock = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)

server_address = "/tmp/socket_file"
print(f"conncting to {server_address}")

try:
    sock.connect(server_address)
except socket.error as err:
    print(err)
    sys.exit(1)

try:
    message = input("Please enter :")
    sock.sendall(message.encode("utf-8"))
    sock.settimeout(2)
    try:
        while True:
            data = sock.recv(4096)

            if data:
                print("Server response:", data)
            else:
                break
    except TimeoutError as err:
        print(err)

finally:
    print("closing socket")
    sock.close()
