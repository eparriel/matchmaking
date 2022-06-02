import socket
import json
import time

import request


class Network:
    def __init__(self):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server = "192.168.1.14"
        self.port = 5555
        self.addr = (self.server, self.port)
        self.status = self.connect()
        self.token = ""

    def getPos(self):
        return self.token

    def connect(self):
        try:
            self.client.connect(self.addr)
            return self.client.recv(2048).decode()
        except:
            pass

    def send(self, data):
        try:
            self.client.send(str.encode(data))

            return self.client.recv(2048).decode()
        except socket.error as e:
            print(e)

    def joinQueue(self, Username):
        queue = request.Request(json.dumps({
            "header": {
                "type": "inQueue",
                "token": self.token,
            },
            "body": {
                "username": Username,
            }
        }))
        return queue

    def signin(self, Username):

        r = request.Request(json.dumps({"header": {
            "type": "signin"
        }, "body": {
            "username": Username,
        }}))
        return r

    def signout(self):
        r = request.Request(json.dumps({"header": {
            "type": "signout",
            "token": self.token,
        }, "body": {
        }}))
        return r


if __name__ == '__main__':
    n = Network()
    username = input("Username: ")
    res = json.loads(
        n.send(
            n.signin(username).getRequest()
        )
    )

    if res["header"]["type"] == "success":
        n.token = res["body"]["token"]
    else:
        print("Invalid username")
        exit(0)

    print(n.token)

    while True:
        toSend = input("-> ")
        if toSend == "exit":
            n.send(n.signout().getRequest())
            n.client.close()
            break
        if toSend == "inQueue":
            print("trying to join the queue")
            while True:
                response = json.loads(
                    n.send(
                        n.joinQueue(username).getRequest())
                )
                print("You are in the queue at the :", response["body"]["position"], "position")
                time.sleep(1)

