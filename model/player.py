# player.py
#
#

from unitmanager import UnitIdGenerator
from unit import Unit

class Player(object):
    def __init__(self, p_id):
        """
        Player object used to track funds throughout game, and list
        statistics of player.
        
        @arg p_id: Player ID
        """
        self.p_id = p_id
        self.units = []

    def GetPID(self):
        """
        Returns the player ID of this player.
        """
        return self.p_id

    def my_unit(self, unit):
        return unit in self.units

    def add_unit_id(self, u_id):
        self.units.append(u_id)

    def get_units(self):
        return self.units
