# playconnect4.py

from gamecontroller import *

def main():
    # gc = TextGameController()
    gc = TextGameControllerEndOnly('TrueRandom', 'SmartRandom')
    gc.playGame()

if __name__ == '__main__':
    main()
