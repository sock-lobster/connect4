# middlesmartrandom.py

from smartrandom import SmartRandom

class MiddleSmartRandom(SmartRandom):
    def placePiece(self):
        # See if anywhere wins
        winningColumn = self.findWinningMove(self.game.board)
        if winningColumn:
            return self.game.board.addPiece(winningColumn, self.number)

        # Only go places that don't lose, with preference for the middle
        safeColumns = self.findNotLosingMoves(self.game.board)
        if safeColumns:
            preferredColumns = [3,2,4,1,5,0,6]
            for column in preferredColumns:
                if column in safeColumns:
                    return self.game.board.addPiece(column, self.number)

        # If not, go random.
        return self.placePieceRandom()
