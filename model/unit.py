# player.py
#
# A player class.

import json

class Unit():
    def __init__(self, spawn_position, _type, uid):
        self.X = spawn_position[0]
        self.Y = spawn_position[1]
        self.Type = _type
        self.uid = uid

    def GetPosition(self):
        return (self.X, self.Y)

    def set_id(self, _id):
        self.uid = _id

    def Move(self, x, y):
        self.X = x
        self.Y = y

    def __str__(self):
        uid = "uID: "+str(self.uid)+", "
        pos = "Position: ["+str(self.X)+", "+str(self.Y)+"], "
        typ = "Type: "+self.Type
        return(uid+pos+typ)
k
