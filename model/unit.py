# player.py
#
# A player class.

import json

class Unit():
    def __init__(self, spawn_position, uid):
        self.X = spawn_position[0]
        self.Y = spawn_position[1]
        self.uid = uid

    def GetPosition(self):
        return (self.X, self.Y)

    def Move(self, x, y):
        self.X = x
        self.Y = y

def UnitGenerator(path):
    f = open(path)
    conf = json.load(f)
    f.close()

    return conf["units"]

def UnitIDGenerator():
    unitIDReference = 0
    while True:
        unitIDReference += 1
        yield unitIDReference
