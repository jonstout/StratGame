# unit.py
#
#

import json

class Unit():
    def __init__(self, conf, p_id, u_id):
        self.X = conf["position"][0]
        self.Y = conf["position"][1]
        
        self.Type = conf["type"]
        self.HP = 10

        self.pid = p_id
        self.uid = u_id

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
        uid = "uID: "+str(self.uid)+", "
        pos = "Position: ["+str(self.X)+", "+str(self.Y)+"], "
        typ = "Type: "+self.Type
        hp = "HP: "+str(self.HP)
        return(uid+pos+typ+hp)
