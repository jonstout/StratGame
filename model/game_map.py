# map.py
#
# A map class.

import json
import random

class GameMap():
    def __init__(self, map_fd):
        f = open(map_fd)
        m = json.load(f)
        f.close()
        
        self.Height = m["dimensions"]["height"]
        self.Width = m["dimensions"]["width"]
        
        self.DefaultUnits = m["units"]
        self.Buildings = m["buildings"]

    def ValidPosition(self, x, y):
        if y >= self.Height or y < 0:
            print("Invalid map position.")
            return False
        if x >= self.Width or x < 0:
            print("Invalid map position.")
            return False
        return True

    def GetBuildings(self):
        return self.Buildings

    def GetDefaultUnits(self):
        return self.DefaultUnits

    def GetDimensions(self):
        return (self.Width, self.Height)
