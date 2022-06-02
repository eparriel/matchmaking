import json


class Request:
    type = ""

    def __init__(self, request):
        self.request = json.loads(request)
        if self.request["header"]["type"] == "action":
            self.type = "action"
        elif self.request["header"]["type"] == "gameInfo":
            self.type = "gameInfo"
        elif self.request["header"]["type"] == "statistique":
            self.type = "statistique"
        elif self.request["header"]["type"] == "inQueue":
            self.type = "inQueue"
        elif self.request["header"]["type"] == "signin":
            self.type = "signin"
        elif self.request["header"]["type"] == "error":
            self.type = "error"
        elif self.request["header"]["type"] == "signout":
            self.type = "signout"
        else:
            self.type = "none"

    def getRequestBody(self):
        return self.request["body"]

    def getRequestHeader(self):
        return self.request["header"]

    def getRequestType(self):
        return self.type

    def getRequest(self):
        return json.dumps(self.request)

    def signin(self, token, username):
        req = json.dumps({"header": {
            "token": token,
            "type": "signin"
        }, "body": {
            "username": username,
        }})
        return req


