from model.unit import Unit

import json

class UnitManager(object):
    def __init__(self):
        """
        A UnitManager is responsible for keeping track of all
        game units.
        {
        "0": [ {"type": "infantry", "position": [1, 1]} ],
        "1": [ {"type": "infantry", "position": [1, 2]} ]
        }
        """
        self.id_generator = UnitIdGenerator()
        self.units = {}

    def add_unit(self, json, player_id):
        """
        Adds a unit to this UnitManager. Returns the unit id
        of the newly created unit.
        """
        _id = self.id_generator.next()
        unit = Unit(json["type"], json["position"], _id, player_id)
        self.units[unit.GetUID()] = unit
        return _id

    def del_unit(self, u_id):
        del( self.units[u_id] )

    def get_unit(self, u_id):
        return self.units[u_id]

    def get_units(self):
        for k in self.units:
            yield self.units[k]

    def my_unit(self, u_id, player_id):
        return self.units[u_id].GetPID() == player_id

    def move_unit(self, u_id, position):
        self.units[u_id].Move(position[0], position[1])
        return True

    def get_position(self, u_id):
        return self.units[u_id].GetPosition()

def UnitIdGenerator():
    _id = 1
    while True:
        _id += 1
        yield _id
