class Request:
    type = ""

    def __init__(self, request):
        self.request = request

    def requestType(self):

        if "type: action" in self.request:
            self.type = "action"
        elif "type: SignUp" in self.request:
            self.type = "SignUp"
        elif "type: authenticate" in self.request:
            self.type = "authenticate"
        elif "type: gameinfo" in self.request:
            self.type = "gameinfo"
        elif "type: statistique" in self.request:
            self.type = "statistique"
        elif "type: inQueue" in self.request:
            self.type = "inQueue"
        else:
            self.type = "none"

        print(self.type)

    def getRequestBody(self):
        return

    def getRequestType(self):
        return self.request


