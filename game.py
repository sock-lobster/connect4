# game.py
# Rules engine for a game of connect 4.

from player import *

class Board(object):
    def __init__(self, width, height):
        self.height = height
        self.width = width
        self.array = [[0]*width for i in range(height)]
        self.testPieces = []

    # Put the player's piece into the board at the desired column
    def addPiece(self, column, player):
        if -1 >= column or column >= self.width:
            raise RuntimeError("Invalid column")
        # Don't put a piece in a full column
        if self.array[self.height-1][column] != 0:
            raise RuntimeError("Full column")
        # Drop the piece as low as it can be in desired column
        else:
            for row in range(self.height):
                if self.array[row][column] == 0:
                    self.array[row][column] = player
                    return {'row':row, 'column':column}

    def addTestPiece(self, column, player):
        self.testPieces.append(self.addPiece(column, player))
        print self.testPieces

    def removeTestPiece(self):
        location = self.testPieces.pop()
        self.array[location['row']][location['column']] = 0

    def removeAllTestPieces(self):
        while len(self.testPieces) > 0:
            self.removeTestPiece()

    def checkWin(self, location, player):
        playerNumber = player.number
        row = location['row']
        column = location['column']

        #Check horozontal
        consecutive = 0
        for i in range(max(0, column-3), min(self.width, column+3)):
            if self.array[row][i] == playerNumber:
                consecutive += 1
                if consecutive == 4:
                    return player
            else:
                consecutive = 0
        #Check vertical
        if (row >= 3 and
            self.array[row][column] == playerNumber and
            self.array[row-1][column] == playerNumber and
            self.array[row-2][column] == playerNumber and
            self.array[row-3][column] == playerNumber):
            return player

        #Check diagonal up

class Game(object):
    def __init__(self, height, width, p1type='Human', p2type='Human'):
        pf = PlayerFactory()
        self.board = Board(width, height)
        self.p1 = pf.makePlayer(p1type, 1, self)
        self.p2 = pf.makePlayer(p2type, 2, self)
        self.turn = 1
        self.winner = None



    def takeTurn(self):
        turnTaker = None
        if self.turn % 2 == 1:
            turnTaker = self.p1
        else:
            turnTaker = self.p2

        location = turnTaker.placePiece()
        winner = self.board.checkWin(location, turnTaker)
        self.turn += 1
        if winner:
            return winner
