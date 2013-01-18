import model.unit

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

    def add_unit(self, unit):
        """
        Adds a unit to this UnitManager. Returns the unit id
        of the newly created unit.
        """
        _id = self.id_generator.next()
        unit.set_id(_id)
        self.units[_id] = unit
        return _id

    def del_unit(self, u_id):
        del( self.units[u_id] )

    def get_unit(self, u_id):
        return self.units[u_id]

    def move_unit(self, u_id, position):
        self.units[u_id].Move(position[0], position[1])

    def get_position(self, u_id):
        return self.units[u_id].GetPosition()

def UnitIdGenerator():
    _id = 1
    while True:
        _id += 1
        yield _id
