# player.py
# player types human/ai/random for a game of connect 4
import random as rand

class PlayerFactory(object):
    def makePlayer(type, number, game):
        if type == 'Human': return Human(number, game)
        if type == 'TrueRandom': return TrueRandom(number, game)
        if type == 'SmartRandom': return SmartRandom(number, game)

    makePlayer = staticmethod(makePlayer)

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

class Human(Player):
    def placePiece(self):
        myTurn = True
        column = None
        placement = None
        while myTurn:
            # This should be moved into the game contollers, this is text game specific.
            # But the player shouldn't care what type of game controller is
            # being used, so I'm not so sure.
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
        column = None
        placement = None
        possibleMoves = range(self.game.board.width)
        while True:
            # Place a piece randomly
            column = rand.choice(possibleMoves)
            try:
                # column = rand.randint(0, self.game.board.width - 1)
                return self.game.board.addPiece(column, self.number)
            except RuntimeError, Argument:
                possibleMoves.remove(column)

class SmartRandom(TrueRandom):
    def findWinningMove(self, board):
        for i in range(board.width):
            try:
                location = board.addTestPiece(i, self.number)
                win = board.checkWin(location, self.number)
                board.removeTestPiece()
                if win:
                    return i
            except RuntimeError, Argument:
                pass

    def findNotLosingMoves(self, board):
        moves = range(board.width)
        for i in range(board.width):
            try:
                location = board.addTestPiece(i, self.number)
                for j in range(board.width):
                    try:
                        location2 = board.addTestPiece(j, self.opponent.number)
                        lose = board.checkWin(location2, self.opponent.number)
                        board.removeTestPiece()
                        if lose:
                            moves.remove(i)
                            break
                    except RuntimeError, Argument:
                        pass
                board.removeTestPiece()
            except RuntimeError, Argument:
                moves.remove(i)
        return moves

    def placePiece(self):
        myTurn = True
        column = None
        placement = None
        # See if anywhere wins
        winningColumn = self.findWinningMove(self.game.board)
        if winningColumn:
            return self.game.board.addPiece(winningColumn, self.number)

        # Only go places that don't lose.
        safeColumns = self.findNotLosingMoves(self.game.board)
        if len(safeColumns) > 0:
            column = rand.choice(safeColumns)
            return self.game.board.addPiece(column, self.number)

        # If not, go random.
        return super(SmartRandom, self).placePiece()
