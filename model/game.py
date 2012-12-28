# game.py
#
#

import string
import unit
from unit import Unit, UnitGenerator, UnitIDGenerator
from gamemap import GameMap
from turns import Turns

class Game(object):
    """ Game
    self.unit_factories - type(map[player_id]UnitFactory)
    - This is a list of all unit factories. This is where
    all units can be built.

    self.game_map - type(GameMap)
    - A representation of the gamemap. Map tiles are stored
    here and can be referenced for movement costs and tile
    type.

    self.players - type(map[player_id]Player)
    - This is where all player related information is stored.
    This includes player_id, score, and money.

    self.turns - type(Turns)
    - This tracks whose turn it is along with total number
    of turns.

    self.units - type(map[player_id]map[unit_id]Unit)
    This holds a map of all units stored by player_id and unit_id.
    Units can attack other players' units (if they're in range)
    and can move to new locations that are not occupied by other
    units.
    """
    def __init__(self, players, a_mtrx, game_map):
        self.game_map = GameMap("./maps/" + game_map + ".json")

        
        self.turns = Turns()
        for i in range( len(players) ):
            self.turns.AddPlayer(i)

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

    def ListUnits(self):
        units = self.players[self.turns.CurrentPlayer()].GetUnits()
        for u in units:
            print(str(units[u]))
    
    def MoveUnit(self, cmd):
        s_parts = string.split(cmd, " ")
        uid = int(s_parts[1])
        pos = string.split(s_parts[2], ".")
        pos[0] = int(pos[0])
        pos[1] = int(pos[1])
        if self.game_map.ValidPosition(pos[0], pos[1]):
            self.players[self.turns.CurrentPlayer()].MoveUnit(uid, pos[0], pos[1])

    def Done(self):
        print("Player" + str(self.turns.CurrentPlayer()) + "'s turn is over.")
        self.turns.NextPlayer()
        print("It's Player" + str(self.turns.CurrentPlayer()) + "'s turn.")

    def AttackUnit(self, cmd):
        s_parts = string.split(cmd, " ")
        uid1 = int(s_parts[1])
        uid2 = int(s_parts[2])

        # Make sure targeted unit is not your own
        if uid1 in self.players[self.turns.CurrentPlayer()].GetUnits():
            print(str(uid1) + " is your own unit. You cannot attack it.")
            return False
        # Make sure attacking unit is owned by current player
        if uid2 not in self.players[self.turns.CurrentPlayer()].GetUnits():
            print(str(uid2) + " is not your unit.")
            return False
        # Units cannot attack themselves
        if uid1 == uid2:
            print("A unit cannot attack itself")
            return False

        u2 = self.players[self.turns.CurrentPlayer()].GetUnit(uid2)
        if u2 != None:
            # Find the uid from players
            for p in self.players:
                u = p.GetUnit(uid1)
                if u != None:
                    if u2.Attack(self.AttackMatrix, u):
                        p.DestroyUnit(uid1)
                        print(str(u) + " was destroyed")
                        return True
                    else:
                        print(str(uid1) + " was hit.")
                        return True
        print("Unit is not attackable")
        return False

    def Run(self):
        print("It's Player" + str(self.turns.CurrentPlayer()) + "'s turn.")

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
