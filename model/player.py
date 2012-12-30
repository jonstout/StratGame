# player.py
#
#

from unit import UnitIDGenerator
from unit import Unit

class Player(object):
    def __init__(self, p_id):
        """
        Player object used to track funds throughout game, and list
        statistics of player.
        
        @arg p_id: Player ID
        """
        self.p_id = p_id

    def GetPID(self):
        """
        Returns the player ID of this player.
        """
        return self.p_id
