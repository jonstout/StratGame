# player.py
#
#

from unit import UnitIDGenerator
from unit import Unit
from units.infantry import Infantry

class Player(object):
    def __init__(self, p_id):
        """
        Player object used to track funds throughout game, and list
        statistics of player.
        
        @arg p_id: Player ID
        @param units: Array of unit IDs owned by player
        
        TODO:
        Make self.units a sorted list.
        """
        self.p_id = p_id
        self.units = []

    def GetPID(self):
        """
        Returns the player ID of this player.
        """
        return self.p_id

    def AddUID(self, u_id):
        """
        Adds u_id to list of unit IDs owned by this player.
        
        @arg u_id: ID of Unit to be added
        """
        self.units.append(u_id)

    def RemoveUID(self, u_id):
        """
        Removes u_id from list of unit IDs owned by this
        player. Usually means the unit represented by this
        unit ID has been destroyed.

        @arg u_id: ID of Unit to be removed
        """
        self.units.remove(u_id)
