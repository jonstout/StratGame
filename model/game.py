# game.py
#
#

from gamemap import GameMap
import unit
from unit import Unit, UnitGenerator

class Game(object):
    def __init__(self, players, game_map):
        self.game_map = GameMap("./maps/" + game_map + ".json")
        self.game_turn = 0
        self.game_on = True

        print("Board Dimensions:", self.game_map.GetDimensions())

        units = UnitGenerator("./maps/" + game_map + ".json")
        if len(units) < len(players):
            self.game_on = False
            print("To many players for this map")
        else:
            for i in range( len(units) ):
                players[i].SetUnits(units[i])
        self.players = players
        
        self.play_counter = 0
        self.current_player = 0

    def NextPlayer(self):
        self.play_counter += 1
        return self.play_counter % len(self.players)

    def ListUnits(self):
        for u in self.players[self.current_player].GetUnits():
            print(u["type"], u["position"])
    
    def Done(self):
        print("Player" + str(self.current_player) + "'s turn is over.")
        self.current_player = self.NextPlayer()
        print("It's Player" + str(self.current_player) + "'s turn.")

    def Run(self):
        print("It's Player" + str(self.current_player) + "'s turn.")

        while self.game_on:
            cmd = raw_input("$ ")

            if cmd == "exit":
                self.game_on = False
            elif cmd == "help":
                print("exit - End program")
                print("help - Print this help message")
                print("list_units - List available units and their location")
                print("done - End player's turn")
            elif cmd == "list_units":
                self.ListUnits()
            elif cmd == "done":
                self.Done()
            else:
                print("Bad command")
        print("Game Over")
