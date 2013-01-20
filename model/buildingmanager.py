from building import Building

class BuildingManager(object):
    def __init__(self, json):
        """
        """
        self.id_generator = BuildingIdGenerator()
        self.buildings = {}

        self.configuration = json

    def add_building(self, json, player_id):
        """
        """
        _id = self.id_generator.next()
        conf = self.configuration[ json["type"] ]
        building = Building(json["type"], json["position"], \
                                conf, _id, player_id)
        self.buildings[building.GetBID()] = building
        return _id

    def capture_building(self, b_id, u_id, u_hp, p_id):
        return self.buildings[b_id].capture(u_id, u_hp, p_id)

    def get_building(self, b_id):
        return self.buildings[b_id]

    def get_buildings(self):
        for k in self.buildings:
            yield self.buildings[k]

    def my_building(self, u_id, player_id):
        return self.buildings[b_id].GetPID() == player_id

def BuildingIdGenerator():
    _id = 399
    while True:
        _id += 1
        yield _id
