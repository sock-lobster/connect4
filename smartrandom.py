#smartrandom.py

from truerandom import TrueRandom
import random as rand
import pdb

class SmartRandom(TrueRandom):
    def __init__(self, number, game, equalOpponent=None):
        super(TrueRandom, self).__init__(number, game)
        # self.number = number
        # self.game = game
        # self.opponent = None
        if equalOpponent:
            self.equalOpponent = equalOpponent
        else:
            self.equalOpponent = SmartRandom((number%2)+1, game, self)

    def findWinningMove(self, board):
        for i in board.openColumns.keys():
            location = board.addTestPiece(i, self.number)
            win = board.checkWin(location, self.number)
            board.removeTestPiece()
            if win:
                return i

    def findNotLosingMoves(self, board):
        moves = board.openColumns.keys()
        for i in board.openColumns.keys():
            board.addTestPiece(i, self.number)

            lose = self.equalOpponent.findWinningMove(board)
            if lose:
                moves.remove(i)

            board.removeTestPiece()

        return moves

    def placePiece(self):
        # See if anywhere wins
        winningColumn = self.findWinningMove(self.game.board)
        if winningColumn:
            return self.game.board.addPiece(winningColumn, self.number)

        # Only go places that don't lose.
        safeColumns = self.findNotLosingMoves(self.game.board)
        if safeColumns:
            column = rand.choice(safeColumns)
            return self.game.board.addPiece(column, self.number)

        # If not, go random.
        return self.placePieceRandom()
