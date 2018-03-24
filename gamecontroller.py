# gamecontroller.py
# plays a game of connect 4, displayTurning as necessary

from game import *

HEIGHT = 6
WIDTH = 7

class GameController(object):
    def __init__(self, p1Type='Human', p2Type='Human'):
        self.game = Game(HEIGHT, WIDTH, p1Type, p2Type)
        self.winner = None

    def playGame(self):
        self.displayTurn()
        while not self.winner:
            self.winner = self.game.takeTurn()
            self.displayTurn()

        self.concludeGame()

class TextGameController(GameController):
    def display(self):
        sprites = {0 : ' ', 1 : '0', 2 : 'X'}
        board = self.game.board.array
        for i in range(HEIGHT-1, -1, -1):
            row = board[i]
            print "|" + "|".join([sprites[j] for j in row]) + "|"
        print "=="*(WIDTH + 1)
        print " "+" ".join(str(k) for k in range(1,WIDTH+1))
    def displayTurn(self):
        self.display()

    def concludeGame(self):
        print str(self.winner) + " wins!"

class TextGameControllerEndOnly(TextGameController):
    def displayTurn(self):
        pass
    def concludeGame(self):
        self.display()
        print str(self.winner) + " wins!"

class GraphicalGameController(GameController):
    def displayTurn(self):
        board = self.game.board.array
        for row in range(HEIGHT, -1, -1):
            print row
        print "man, this was supposed to look nice..."
