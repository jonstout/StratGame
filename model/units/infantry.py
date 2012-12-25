# infantry.py
#
#

from ..unit import Unit

class Infantry(Unit):
    def __init__(self, spawn_position, uid):
        Unit.__init__(self, spawn_position, "infantry", uid)

        self.Type = "infantry"
        self.AP = 10
        self.HP = 10

    def Attack(self, a_mtrx, unit):
        """ Attack(attack_matrix, unitID)
        Returns True if unit is destroyed, else False.
        """
        unit.HP -= int(float(a_mtrx[self.Type][unit.Type])*self.AP)
        if unit.HP <= 0:
            return True
        return False

    def __str__(self):
        uid = "uID: "+str(self.uid)+", "
        pos = "Position: ["+str(self.X)+", "+str(self.Y)+"], "
        typ = "Type: "+self.Type+", "
        hp = "HP: "+str(self.HP)+", "
        ap = "AP: "+str(self.AP)
        return(uid+pos+typ+hp+ap)
