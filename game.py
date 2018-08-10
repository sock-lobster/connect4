# game.py
# Rules engine for a game of connect 4.

from playerfactory import PlayerFactory
import pdb, traceback

class Board(object):
    def __init__(self, width, height):
        self.height = height
        self.width = width
        self.array = [[0]*width for i in range(height)]
        self.testPieces = []
        self.openColumns = dict(zip(range(self.width), [1]*self.width))

    def __repr__(self):
        printstr = ''
        sprites = {0 : ' ', 1 : '0', 2 : 'X'}
        for i in range(self.height-1, -1, -1):
            row = self.array[i]
            printstr += "|" + "|".join([sprites[j] for j in row]) + "|\n"
        printstr += "=="*(self.width + 1) + "\n"
        printstr += " "+" ".join(str(k) for k in range(1,self.width+1))
        return printstr

    # Put the player's piece into the board at the desired column
    def addPiece(self, column, player, test=False):
        if not test:
            # traceback.print_stack()
            assert len(self.testPieces) == 0, "real pieces on test pieces."
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
                    if row == self.height - 1:
                        del self.openColumns[column]
                    return {'row':row, 'column':column}

    def addTestPiece(self, column, player):
        location = self.addPiece(column, player, True)
        self.testPieces.append(location)
        return location

    def removeTestPiece(self):
        location = self.testPieces.pop()
        self.array[location['row']][location['column']] = 0
        self.openColumns[location['column']] = 1

    def removeAllTestPieces(self):
        while len(self.testPieces) > 0:
            self.removeTestPiece()

    def checkConsecutive(self, location, minus, plus, operations, player):
        consecutive = 0
        row = location['row']
        column = location['column']
        rowop = operations['row']
        colop = operations['col']
        for i in range(minus, plus):
            if self.array[row+i*rowop][column+i*colop] == player:
                consecutive += 1
                if consecutive == 4:
                    return True
            else:
                consecutive = 0
        return False

    def checkWin(self, location, player):
        row = location['row']
        column = location['column']

        # Check vertical
        minus = -min(row, 3)
        plus = min(self.height-row, 4)
        operations = {'row': 1, 'col': 0}
        if self.checkConsecutive(location, minus, plus, operations, player):
            return player

        # Check horozontal
        minus = -min(column, 3)
        plus = min(self.width-column, 4)
        operations = {'row': 0, 'col': 1}
        if self.checkConsecutive(location, minus, plus, operations, player):
            return player

        # Check diagonal up
        minus = -min(row, column, 3)
        plus = min(self.height-row, self.width-column, 4)
        operations = {'row': 1, 'col': 1}
        if self.checkConsecutive(location, minus, plus, operations, player):
            return player

        # Check diagonal down
        minus = -min(self.height-row-1, column, 3)
        plus = min(row+1, self.width-column, 4)
        operations = {'row': -1, 'col': 1}
        if self.checkConsecutive(location, minus, plus, operations, player):
            return player

class Game(object):
    def __init__(self, height, width, p1type, p2type):
        pf = PlayerFactory()
        self.board = Board(width, height)
        self.p1 = pf.makePlayer(p1type, 1, self)
        self.p2 = pf.makePlayer(p2type, 2, self)
        self.draw = pf.makePlayer('Draw', 0, self)
        self.p1.setOpponents(self.p2)
        self.turn = 1
        self.winner = None

    def takeTurn(self):
        turnTaker = None
        if self.turn % 2 == 1:
            turnTaker = self.p1
        else:
            turnTaker = self.p2

        location = turnTaker.placePiece()
        self.turn += 1

        win = self.board.checkWin(location, turnTaker.number)
        if win:
            return turnTaker

        if self.turn > self.board.height * self.board.width:
            return Draw()
