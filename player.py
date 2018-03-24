# player.py
# player types human/ai/random for a game of connect 4
import random as rand

class PlayerFactory(object):
    def makePlayer(type, number, game):
        if type == 'Human': return Human(number, game)
        if type == 'TrueRandom': return TrueRandom(number, game)

    makePlayer = staticmethod(makePlayer)

class Player(object):
    def __init__(self, number, game):
        self.number = number
        self.game = game

    def __repr__(self):
        return "player {} the {}".format(self.number, type(self).__name__)

class Draw(Player):
    def __init__(self):
        self.number = 0

class Human(Player):
    def placePiece(self):
        myTurn = True
        column = None
        placement = None
        while myTurn:
            # This should be moved into the game contollers, this is text game specific.
            try:
                inputtext = '\nPlayer {} what column would you like? '.format(self.number)
                column = int(raw_input(inputtext))-1
                return self.game.board.addPiece(column, self.number)
            except ValueError, Argument:
                print "You must input an integer."
            except RuntimeError, Argument:
                print Argument

class TrueRandom(Player):
    def placePiece(self):
        myTurn = True
        column = None
        placement = None
        while myTurn:
            # This should be moved into the game contollers, this is text game specific.
            try:
                # inputtext = '\nPlayer {} what column would you like? '.format(self.number)
                column = rand.randint(0,6)
                return self.game.board.addPiece(column, self.number)
            except RuntimeError, Argument:
                pass
