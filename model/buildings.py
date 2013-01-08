import json

class Building(object):
    def __init__(self, pid, conf):
        self.pid = pid
        
        self.Type = conf["type"]
        self.X = conf["position"][0]
        self.Y = conf["position"][1]
