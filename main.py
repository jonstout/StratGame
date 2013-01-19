# Advance Wars Clone

import os

from model.game import Game
from model.game_map import GameMap
from model.player import Player
from model.turns import Turns
from model.unit import Unit
from model.unitmanager import UnitManager
from model.unitmanager import UnitIdGenerator
from model.configuration import Configuration

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

    g = Game(config, game_map, players, turns, unit_manager)
    g.Run()
