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

    def checkConsecutive(self, location, minus, plus, operations, playerNum):
        consecutive = 0
        row = location['row']
        column = location['column']
        rowop = operations['row']
        colop = operations['col']
        for i in range(minus, plus):
            if self.array[row+i*rowop][column+i*colop] == playerNum:
                consecutive += 1
                if consecutive == 4:
                    return True
            else:
                consecutive = 0
        return False

    def checkWin(self, location, player):
        playerNum = player.number
        row = location['row']
        column = location['column']

        # Check vertical
        minus = -min(row, 3)
        plus = min(self.height-row, 4)
        operations = {'row': 1, 'col': 0}
        if self.checkConsecutive(location, minus, plus, operations, playerNum):
            return player
        # consecutive = 0
        # for i in range(minus, plus):
        #     if self.array[row+i][column] == playerNum:
        #         consecutive += 1
        #         if consecutive == 4:
        #             return player
        #     else:
        #         consecutive = 0
        # if (row >= 3 and
        #     self.array[row][column] == playerNum and
        #     self.array[row-1][column] == playerNum and
        #     self.array[row-2][column] == playerNum and
        #     self.array[row-3][column] == playerNum):
        #
        #     return player

        # Check horozontal
        minus = -min(column, 3)
        plus = min(self.width-column, 4)
        operations = {'row': 0, 'col': 1}
        if self.checkConsecutive(location, minus, plus, operations, playerNum):
            return player
        # consecutive = 0
        # for i in range(minus, plus):
        #     if self.array[row][column+i] == playerNum:
        #         consecutive += 1
        #         if consecutive == 4:
        #             return player
        #     else:
        #         consecutive = 0

        # Check diagonal up
        minus = -min(row, column, 3)
        plus = min(self.height-row, self.width-column, 4)
        operations = {'row': 1, 'col': 1}
        if self.checkConsecutive(location, minus, plus, operations, playerNum):
            return player
        # consecutive = 0
        # for i in range(minus, plus):
        #     if self.array[row+i][column+i] == playerNum:
        #         consecutive += 1
        #         if consecutive == 4:
        #             return player
        #     else:
        #         consecutive = 0

        # Check diagonal down
        minus = -min(self.height-row-1, column, 3)
        plus = min(row+1, self.width-column, 4)
        operations = {'row': -1, 'col': 1}
        if self.checkConsecutive(location, minus, plus, operations, playerNum):
            return player
        # consecutive = 0
        # for i in range(minus, plus):
        #     if self.array[row-i][column+i] == playerNum:
        #         consecutive += 1
        #         if consecutive == 4:
        #             return player
        #     else:
        #         consecutive = 0

class Game(object):
    def __init__(self, height, width, p1type, p2type):
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

        if self.turn > self.board.height * self.board.width:
            return Draw()
