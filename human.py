# human.py

# import player as play
from player import Player

class Human(Player):
    def placePiece(self):
        while True:
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
