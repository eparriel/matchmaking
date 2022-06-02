class Queue:
    queue = []

    def addPlayer(self, playerId):
        if self.queue.index(playerId) < 0:
            self.queue.append(playerId)
        else:
            print("player already in queue")

    def lauchGame(self):
        players = []
        if len(self.queue) > 1:
            players = [self.queue[0], self.queue[1]]
            self.queue.pop(0)
            self.queue.pop(0)
        else:
            print("we need more players to launch a game")

        return players

