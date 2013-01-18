# Advance Wars Clone

import os

from model.game import Game
from model.game_map import GameMap
from model.player import Player
from model.turns import Turns
from model.unit import Unit
from model.unitmanager import UnitManager
from model.unitmanager import UnitIdGenerator
from model.attack_matrix import AttackMatrix

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

    attack_matrix = AttackMatrix("./model/units.json")
    game_map = GameMap("./maps/" + selected_map + ".json")

    players = [Player(1), Player(2)]

    """
    turns = Turns()
    units = {}

    if len(players) == game_map.GetNumberOfPlayers():
        d_units = game_map.GetDefaultUnits()
        u_gen = UnitIdGenerator()

        for i in range( len(players) ):
            p_id = players[i].GetPID()
            turns.AddPlayer(p_id)
            for u in d_units[i]:
                unit = Unit(u, p_id, u_gen.next())
                units[unit.GetUID()] = unit

    """
    game_units = game_map.GetDefaultUnits()
    unit_manager = UnitManager()
    
    for player_id in game_units:
        for unit in game_units[player_id]:
            unit_manager.add_unit(unit, int(player_id))

    print(unit_manager)

    #g = Game(attack_matrix, game_map, players, turns, units)
    #g.Run()
