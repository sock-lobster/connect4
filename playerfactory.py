#playerfactory.py

from player import Player, Draw
from truerandom import TrueRandom
from smartrandom import SmartRandom
from middlesmartrandom import MiddleSmartRandom
from human import Human

class PlayerFactory(object):
    def makePlayer(type, number, game):
        if type == 'Human': return Human(number, game)
        if type == 'TrueRandom': return TrueRandom(number, game)
        if type == 'SmartRandom': return SmartRandom(number, game)
        if type == 'MiddleSmartRandom': return MiddleSmartRandom(number, game)
        if type == 'Draw': return Draw()

    makePlayer = staticmethod(makePlayer)
