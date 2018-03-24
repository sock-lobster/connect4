# gamecontroller.py
# plays a game of connect 4, displaying as necessary

from game import *

HEIGHT = 6
WIDTH = 7

class GameController(object):
    def __init__(self):
        self.game = Game(HEIGHT, WIDTH)

    def playGame(self):
        winner = None
        self.display()
        while not winner:
            winner = self.game.takeTurn()
            self.display()
        print str(winner) + " wins!"

class TextGameController(GameController):
    def display(self):
        sprites = {0 : ' ', 1 : '0', 2 : 'X'}
        board = self.game.board.array
        for i in range(HEIGHT-1, -1, -1):
            row = board[i]
            print "|" + "|".join([sprites[j] for j in row]) + "|"
        print "=="*(WIDTH + 1)
        print " "+" ".join(str(k) for k in range(1,WIDTH+1))



class GraphicalGameController(GameController):
    def display(self):
        board = self.game.board.array
        for row in range(HEIGHT, -1, -1):
            print row
        print "man, this was supposed to look nice..."
