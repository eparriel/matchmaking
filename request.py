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
        else:
            self.type = "none"

        print(self.type)

    def getRequestBody(self):
        return

    def getRequest(self):
        return json.dumps(self.request)


