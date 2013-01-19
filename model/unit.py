# unit.py
#
#

import json

class Unit():
    def __init__(self, _type, _position, _id, player_id):
        self.X = _position[0]
        self.Y = _position[1]
        
        self.Type = _type
        self.HP = 10

        self.pid = player_id
        self.uid = _id

    def GetPID(self):
        return self.pid

    def GetUID(self):
        return self.uid

    def GetHP(self):
        return self.HP

    def GetPosition(self):
        return (self.X, self.Y)

    def GetType(self):
        return self.Type

    def set_id(self, _id):
        self.uid = _id

    def Move(self, x, y):
        self.X = x
        self.Y = y
        print("UnitID "+str(self.uid)+": moved")

    def Defend(self, u_hp, u_attack_multiplier):
        """ Decreases this unit's HP

        @arg u_hp: HP of attacking unit
        @arg u_attack_multiplier: Attack mult. of attacking unit
        """
        self.HP -= int( float(u_attack_multiplier) * u_hp )

        if self.HP > 0:
            print("Unit "+str(self.uid)+": "+str(self.HP)+" life left")
            return True
        else:
            print("Destroyed Unit "+str(self.uid))
            return False

    def __str__(self):
        uid = "uID: {}, ".format(self.uid)
        pos = "Position: [{}, {}], ".format(self.X, self.Y)
        typ = "Type: {}, ".format(self.Type)
        hp = "HP: {} ".format(self.HP)
        return(uid+pos+typ+hp)
