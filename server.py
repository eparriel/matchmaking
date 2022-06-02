import socket
from _thread import *
import sys
import random
import string

server = "192.168.1.14"
port = 5555

ONLINE_USERS = []
INQUEUE = []

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    s.bind((server, port))
except socket.error as e:
    str(e)

s.listen(10)
print("Waiting for a connection, Server Started")


def threaded_client(conn, token, addr):
    conn.send(str.encode(token))
    ONLINE_USERS.append({"token": token, "addr": addr})
    print("players online: ", len(ONLINE_USERS))
    reply = ""
    while True:
        try:
            data = conn.recv(2048)
            reply = data.decode()

            if not data:
                print("PLayer: ", addr, " Disconnected")
                ONLINE_USERS.remove({"token": token, "addr": addr})
                print("players online: ", len(ONLINE_USERS))
                break
            else:
                print("Received: ", reply)
                print("Sending : ", reply)

            conn.sendall(str.encode(reply))
        except:
            break

    print("Lost connection")
    conn.close()


while True:
    conn, addr = s.accept()
    token = ''.join(random.choices(string.ascii_lowercase, k=10))
    print("Connected to:", addr)
    start_new_thread(threaded_client, (conn, token, addr))


