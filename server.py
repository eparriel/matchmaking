import socket
from _thread import *
import sqlite3
import sys
import string
import json
import request
import random

server = "127.0.0.1"
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


def reqSignin(conn, addr, req, db, cur):
    print("Player: ", req.getRequestBody()["username"], " has signin")
    token = ''.join(random.choices(string.ascii_lowercase, k=20))
    if req.getRequestBody()["username"] == "":
        return str.encode(
            json.dumps({"header": {
                "type": "error"
            }, "body": {
            }})
        )
    # a = cur.execute("SELECT username WHERE username = ?", (req.getRequestBody()["username"],))
    #
    # if len(a) > 0:
    #     return str.encode(
    #         json.dumps({"header": {
    #             "type": "error"
    #         }, "body": {
    #         }})
    #     )
    # # add to database
    # cur.execute("INSERT INTO User (username, token) VALUES (?, ?)", (req.getRequestBody()["username"], token))
    ONLINE_USERS.append({"token": token, "addr": addr})

    print("players online: ", len(ONLINE_USERS))
    return str.encode(
        json.dumps({"header": {
            "token": token,
            "type": "success"
        }, "body": {
            "token": token
        }})
    )


def signOut(req, adr):
    ONLINE_USERS.remove({"token": req.getRequestHeader()["token"], "addr": adr})

    try:
        INQUEUE.remove({"token": req.getRequestHeader()["token"], "addr": adr})
    except:
        pass
    return str.encode(
        json.dumps({"header": {
            "type": "success"
        }, "body": {
        }})
    )


def joinTheQueue(req, address):
    try:
        INQUEUE.index({"token": req.getRequestHeader()["token"], "addr": address})
        print("players in queue: ", len(INQUEUE))
    except:
        INQUEUE.append({"token": req.getRequestHeader()["token"], "addr": address})
    return str.encode(
        json.dumps({"header": {
            "token": req.getRequestHeader()["token"],
            "type": "success"
        }, "body": {
            "position": INQUEUE.index({"token": req.getRequestHeader()["token"], "addr": address}) + 1
        }})
    )


def threaded_client(conn, addr, db, cur):
    conn.send(str.encode("Connected"))
    # print("players online: ", len(ONLINE_USERS))
    reply = ""
    while True:
        try:
            data = conn.recv(2048)
            reply = data.decode()

            if not data:
                print("PLayer: ", addr, " Disconnected")
                print("players online: ", len(ONLINE_USERS))
                break
            else:
                token = ""
                req = request.Request(reply)
                print(req.getRequest())
                print(req.getRequestType())

                if req.getRequestType() == "signin":
                    conn.sendall(reqSignin(conn, addr, req, db, cur))

                # if req.getRequestType() == "action":
                #     print("Player: ", req.getRequestBody()["username"], " has action")
                # if req.getRequestType() == "gameInfo":
                #     print("Player: ", req.getRequestBody()["username"], " has gameInfo")
                # if req.getRequestType() == "statistique":
                #     print("Player: ", req.getRequestBody()["username"], " has statistique")

                if req.getRequestType() == "inQueue":
                    conn.sendall(joinTheQueue(req, addr))
                    print("NB players in queue: ", len(INQUEUE))

                if req.getRequestType() == "signout":
                    conn.sendall(signOut(req, addr))
                    print("players online: ", len(ONLINE_USERS))

                print("Received: ", json.dumps(req.getRequest()))
        except:
            break

    print("Lost connection")
    try:
        ONLINE_USERS.remove({"token": req.getRequestHeader()["token"], "addr": addr})
        INQUEUE.remove({"token": req.getRequestHeader()["token"], "addr": addr})
    except:
        pass
    print()
    conn.close()


if __name__ == '__main__':
    # connect to database
    db = sqlite3.connect('db.sqlite')
    cur = db.cursor()

    while True:
        conn, addr = s.accept()
        print("Connected to:", addr)
        start_new_thread(threaded_client, (conn, addr, db, cur))
