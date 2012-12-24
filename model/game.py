# game.py
#
#

import string
import unit
from unit import Unit, UnitGenerator, UnitIDGenerator
from gamemap import GameMap

class Game(object):
    def __init__(self, players, a_mtrx, game_map):
        self.game_map = GameMap("./maps/" + game_map + ".json")
        self.game_turn = 0
        self.game_on = True

        print("Board Dimensions:", self.game_map.GetDimensions())

        self.AttackMatrix = a_mtrx

        self.uid_generator = UnitIDGenerator()
        units = UnitGenerator("./maps/" + game_map + ".json")
        if len(units) < len(players):
            self.game_on = False
            print("To many players for this map")
        else:
            for i in range( len(units) ):
                players[i].SetUnits(units[i], self.uid_generator)
        self.players = players
        
        self.play_counter = 0
        self.current_player = 0

    def NextPlayer(self):
        self.play_counter += 1
        return self.play_counter % len(self.players)

    def ListUnits(self):
        units = self.players[self.current_player].GetUnits()
        for u in units:
            print(str(units[u]))
    
    def MoveUnit(self, cmd):
        s_parts = string.split(cmd, " ")
        uid = int(s_parts[1])
        pos = string.split(s_parts[2], ".")
        pos[0] = int(pos[0])
        pos[1] = int(pos[1])
        if self.game_map.ValidPosition(pos[0], pos[1]):
            self.players[self.current_player].MoveUnit(uid, pos[0], pos[1])

    def Done(self):
        print("Player" + str(self.current_player) + "'s turn is over.")
        self.current_player = self.NextPlayer()
        print("It's Player" + str(self.current_player) + "'s turn.")

    def AttackUnit(self, cmd):
        s_parts = string.split(cmd, " ")
        uid1 = int(s_parts[1])
        uid2 = int(s_parts[2])
        u1 = self.players[self.current_player].GetUnit(uid1)

        # Find the uid from players
        u2 = None
        for p in self.players:
            u = self.players[self.current_player].GetUnit(uid2)
            if u != None:
                if u1.Attack(self.AttackMatrix, u):
                    print(str(uid2) + " was destroyed")
                    u2 = True
                else:
                    print(str(uid2) + " was hit.")
                    u2 = True
        if not u2:
            print("Unit is not attackable")
            return False


    def Run(self):
        print("It's Player" + str(self.current_player) + "'s turn.")

        # Start game command loop
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
            elif cmd[:9] == "move_unit":
                self.MoveUnit(cmd)
            elif cmd[:11] == "attack_unit":
                self.AttackUnit(cmd)
            elif cmd == "done":
                self.Done()
            else:
                print("Bad command")

        # Game loop has been broken by exit command
        print("Game Over")
