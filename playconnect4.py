# playconnect4.py

from gamecontroller import *

def main():
    # gc = TextGameController()
    gc = TextGameControllerEndOnly('TrueRandom', 'TrueRandom')
    gc.playGame()

if __name__ == '__main__':
    main()
