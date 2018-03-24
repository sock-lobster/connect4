# player.py
# player types human/ai/random for a game of connect 4

class PlayerFactory(object):
    def makePlayer(type, number, game):
        if type == 'Human': return Human(number, game)

    makePlayer = staticmethod(makePlayer)

class Player(object):
    def __init__(self, number, game):
        self.number = number
        self.game = game

    def __repr__(self):
        return "player {} the {}".format(self.number, type(self).__name__)

class Human(Player):
    def placePiece(self):
        myTurn = True
        column = None
        placement = None
        while myTurn:
            # This should be moved into the game contollers, this is text game specific.
            try:
                column = int(raw_input('\nPlayer {} what column would you like? '.format(self.number)))-1
                return self.game.board.addPiece(column, self.number)
            except ValueError, Argument:
                print "You must input an integer."
            except RuntimeError, Argument:
                print Argument
