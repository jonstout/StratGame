# attack_matrix
#
#

import json

class AttackMatrix(object):
    def __init__(self, fd):
        f = open(fd)
        self.attack_matrix = json.load(f)
        f.close()

    def GetAttackMultiplier(self, au_type, du_type):
        return self.attack_matrix[au_type][du_type]
