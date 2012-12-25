# player.py
#
#

from unit import UnitIDGenerator
from unit import Unit
from units.infantry import Infantry

class Player(object):
    def __init__(self, name):
        self.name = str(name)
        self.units = {}

    def SetUnits(self, units, uid_generator):
        for u in units:
            i = uid_generator.next()
            u_obj = Unit(u["position"], u["type"], i)

            if u["type"] == "infantry":
                u_obj = Infantry(u["position"], i)
            else:
                u_obj = Unit(u["position"], u["type"], i)
            self.units[i] = u_obj

    def DestroyUnit(self, uid):
        del(self.units[uid])

    def GetUnit(self, uid):
        try:
            return self.units[int(uid)]
        except KeyError:
            return None

    def GetUnits(self):
        return self.units

    def MoveUnit(self, uid, x, y):
        self.units[uid].Move(x, y)
