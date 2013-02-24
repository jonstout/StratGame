from building import Building

class BuildingManager(object):
    def __init__(self, json):
        """
        BuildingManager is responsible for tracking all
        buildings.
        """
        self.id_generator = BuildingIdGenerator()
        self.buildings = {}

        self.configuration = json

    def add_building(self, json, player_id):
        """
        Builds a building from the json config.
        """
        _id = self.id_generator.next()
        conf = self.configuration[ json["type"] ]
        building = Building(json["type"], json["position"], \
                                conf, _id, player_id)
        self.buildings[_id] = building
        return _id

    def capture_building(self, b_id, p_id, u_hp):
        """
        Attempts to capture self.buildings[b_id] for player p_id
        with u
        """
        return self.buildings[b_id].capture(p_id, u_hp)

    def get_building(self, b_id):
        return self.buildings[b_id]

    def get_buildings(self):
        return self.buildings

    def my_building(self, b_id, player_id):
        return self.buildings[b_id].GetPID() == player_id

def BuildingIdGenerator():
    _id = 399
    while True:
        _id += 1
        yield _id
