from faker import Faker
import socket
import os
import json

fake = Faker()
config = json.load(open("config.json"))
sock = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
server_address = open(config["filepath"], "r")

try:
    os.unlink(server_address)
except FileNotFoundError:
    pass

print("Starting up on {}".format(server_address))

sock.bind(server_address)
sock.listen(1)

while True:
    connection, client_address = sock.accept()
    try:
        print("connection from :", client_address)
        while True:
            data = connection.recv(4096)
            data_str = data.decode()
            print("Received", data_str)
            text = fake.sentence()
            print("Add text:", text)
            data_str += " " + text
            if data:
                response = "Processing :" + data_str
                connection.sendall(response.encode())
            else:
                print("no data from", client_address)
                break

    finally:
        print("Closing current connection\n")
        connection.close()
