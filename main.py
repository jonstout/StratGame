# Advance Wars Clone

import os

from model.game import Game
from model.player import Player
from util.attack_matrix import BuildAttackMatrix

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
    game_map = SelectGameMap()

    p1 = Player(1)
    p2 = Player(2)

    a = BuildAttackMatrix("./model/units/units.json")
    g = Game([p1,p2], a, game_map)
    g.Run()
