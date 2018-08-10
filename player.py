# player.py
# player types human/ai/random for a game of connect 4

class Player(object):
    def __init__(self, number, game):
        self.number = number
        self.game = game
        self.opponent = None

    def __repr__(self):
        return "player {} the {}".format(self.number, type(self).__name__)

    def setOpponents(self, other):
        self.opponent = other
        other.opponent = self

    def findWinningMove(self):
        return

    def findNotLosingMoves(self):
        return

class Draw(Player):
    def __init__(self):
        self.number = 0
