# player.py
#
#

from unit import UnitIDGenerator

class Player(object):
    def __init__(self, name):
        self.name = str(name)
        self.units = {}

    def SetUnits(self, units):
        uid = UnitIDGenerator()

        for u in units:
            i = uid.next()
            self.units[i] = u
            self.units[i]["uid"] = i

    def GetUnits(self):
        return self.units

    def MoveUnit(self, uid, x, y):
        self.units[uid].Move(x, y)
