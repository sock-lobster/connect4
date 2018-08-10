# playconnect4.py

from gamecontroller import *
import argparse



def main():
    parser = argparse.ArgumentParser(description='Play a game of connect 4.')
    player_choices = ['Human', 'TrueRandom', 'SmartRandom', 'MiddleSmartRandom']
    parser.add_argument('--p1', default="Human", choices=player_choices)
    parser.add_argument('--p2', default="Human", choices=player_choices)
    args = vars(parser.parse_args())

    gc = TextGameController(args['p1'], args['p2'])
    gc.playGame()

if __name__ == '__main__':
    main()
