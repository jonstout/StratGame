# @author Jonathan Stout

import json

class Configuration(object):
    def __init__(self, fd):
        f = open(fd)
        self.config = json.load(f)
        f.close()

    def GetAttackMultiplier(self, au_type, du_type):
        return self.config["units"][au_type]["attack_matrix"][du_type]

    def GetBuildingsConfig(self):
        return self.config["buildings"]

    def GetGamemapSource(self, _id):
    	return self.config["maps"][_id]

    def GetGamemaps(self):
    	return self.config["maps"]
