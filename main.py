# @author Jonathan Stout

import os

from model.game import Game
from model.game_map import GameMap
from model.player import Player
from model.turns import Turns
from model.unit import Unit
from model.unitmanager import UnitManager
from model.configuration import Configuration
from model.buildingmanager import BuildingManager

def SelectGameMap():
    game_maps = os.listdir("./maps/")
    valid_selections = []
    print("Game Maps")

    for g in game_maps:
        print("- " + g[:-5])
        valid_selections.append(g[:-5])

    while True:
        i = raw_input("$ ")
        if i in valid_selections:
            return i

if __name__ == "__main__":
    selected_map = SelectGameMap()

    
    config = Configuration("./config.json")
    game_map = GameMap("./maps/" + selected_map + ".json")

    players = [Player(1), Player(2)]
    turns = Turns()

    game_units = game_map.GetDefaultUnits()
    unit_manager = UnitManager()
    for player_id in game_units:
        turns.AddPlayer( int(player_id) )
        for unit in game_units[player_id]:
            unit_manager.add_unit(unit, int(player_id))

    game_buildings = game_map.GetBuildings()
    building_manager = BuildingManager(config.GetBuildingsConfig())
    for player_id in game_buildings:
        for build in game_buildings[player_id]:
            building_manager.add_building(build, int(player_id))

    g = Game(config, game_map, players, turns, unit_manager, building_manager)
    g.Run()
