import socket
import json
import request

class Network:
    def __init__(self):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server = "192.168.1.14"
        self.port = 5555
        self.addr = (self.server, self.port)
        self.token = self.connect()
        print(self.token)

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


if __name__ == '__main__':
    n = Network()
    while True:
        toSend = input("-> ")

        req = request.Request(json.dumps({"header": {
            "token": n.getPos(),
            "type": toSend
        }, "body": {
            "x": 0
        }}))
        res = json.loads(n.send(req.getRequest()))
        # print(res['header'])
