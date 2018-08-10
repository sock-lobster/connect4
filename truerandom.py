# truerandom.py

from player import Player
import random as rand

class TrueRandom(Player):
    def placePieceRandom(self):
        possibleMoves = self.game.board.openColumns.keys()
        # Place a piece randomly
        column = rand.choice(possibleMoves)
        return self.game.board.addPiece(column, self.number)

    def placePiece(self):
        return self.placePieceRandom()
