# player.py
#
#

class Player(object):
    def __init__(self, name):
        self.name = str(name)
        self.units = []

    def SetUnits(self, units):
        self.units = units

    def GetUnits(self):
        return self.units
