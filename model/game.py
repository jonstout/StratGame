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
    def __init__(self, attack_matrix, game_map, players, turns, units):
        self.attack_matrix = attack_matrix
        self.game_map = game_map
        self.players = players
        self.turns = turns
        self.units = units
        
        self.game_on = True

        print("Board Dimensions:", self.game_map.GetDimensions())

    def ListUnits(self):
        for u in self.units:
            if self.units[u].GetPID() == self.turns.CurrentPlayer():
                print( str(self.units[u]) )
    
    def MoveUnit(self, cmd):
        s_parts = string.split(cmd, " ")
        uid = int(s_parts[1])
        pos = string.split(s_parts[2], ".")
        pos[0] = int(pos[0])
        pos[1] = int(pos[1])
        if self.game_map.ValidPosition(pos[0], pos[1]) and \
                self.units[uid].GetPID() == self.turns.CurrentPlayer():
            self.units[uid].Move(pos[0], pos[1])

    def Done(self):
        print("Player" + str(self.turns.CurrentPlayer()) + "'s turn is over.")
        self.turns.NextPlayer()
        print("It's Player" + str(self.turns.CurrentPlayer()) + "'s turn.")

    def AttackUnit(self, cmd):
        s_parts = string.split(cmd, " ")
        try:
            unit1 = self.units[ int(s_parts[1]) ]
            unit2 = self.units[ int(s_parts[2]) ]
        except KeyError as e:
            print("Invalid UnitID: "+str(e))
            return False

        # Make sure targeted unit is not your own
        if unit1.GetPID() == self.turns.CurrentPlayer():
            print(str(unit1.GetUID()) + " is your own unit. You cannot attack it.")
            return False
        # Make sure attacking unit is owned by current player
        if unit2.GetPID() != self.turns.CurrentPlayer():
            print(str(unit2.GetUID()) + " is not your unit.")
            return False
        # Units cannot attack themselves
        if unit1.GetUID() == unit2.GetUID():
            print("A unit cannot attack itself")
            return False

        u1_type = unit1.GetType()
        u2_type = unit2.GetType()

        atk_mult = self.attack_matrix.GetAttackMultiplier(u1_type, u2_type)

        # If unit1 was unable to defend remove from game
        if not unit1.Defend(unit2.GetHP(), atk_mult):
            del(self.units[unit1.GetUID()])

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
                print("attack_unit <u1> <u2> - Attack unit u1 with unit u2")
                print("move_unit <u1> <x>.<y> - Move unit u1 to position (x, y)")
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
