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
        self.Dimensions = (self.Width, self.Height)
        
        self.SpawnPositions = m["spawn_positions"]

    def ValidPosition(self, x, y):
        if y >= self.Height or y < 0:
            print("Invalid map position.")
            return False
        if x >= self.Width or x < 0:
            print("Invalid map position.")
            return False
        return True

    def GetDimensions(self):
        return self.Dimensions

    def GetSpawnPosition(self):
        i = random.randint(0, len(self.SpawnPositions) - 1)
        if self.ValidPosition(self.SpawnPositions[i][0], self.SpawnPositions[i][1]):
            return self.SpawnPositions[i]
        else:
            print("Invalid spawn position")
            raise ValueError
