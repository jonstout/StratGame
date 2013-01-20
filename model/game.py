# @author Jonathan Stout

import string

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
    def __init__(self, attack_matrix, game_map, players, turns, unit_manager, building_manager):
        self.attack_matrix = attack_matrix
        self.game_map = game_map
        self.players = players
        self.turns = turns
        self.units = unit_manager
        self.buildings = building_manager
        self.game_on = True

        print("Board Dimensions:", self.game_map.GetDimensions())

    def ListUnits(self):
        """
        Lists all units in the game. Of course you can only use
        your game units.
        """
        for u in self.units.get_units():
            print u
    
    def MoveUnit(self, cmd):
        """
        Moves a unit if the movement is valid. Returns True if a
        valid move; Else False.
        """
        s_parts = string.split(cmd, " ")
        uid = int(s_parts[1])
        pos = string.split(s_parts[2], ".")
        pos[0] = int(pos[0])
        pos[1] = int(pos[1])
        if self.units.my_unit(uid, self.turns.CurrentPlayer()) and \
                self.game_map.ValidPosition(pos[0], pos[1]):
            return self.units.move_unit(uid, pos)
        return False

    def Done(self):
        print("Player" + str(self.turns.CurrentPlayer()) + "'s turn is over.")
        print("It's Player" + str(self.turns.NextPlayer()) + "'s turn.")

    def AttackUnit(self, cmd):
        s_parts = string.split(cmd, " ")

        d_unit = self.units.get_unit( int(s_parts[1]) )
        a_unit = self.units.get_unit( int(s_parts[2]) )
        # Make sure attacking unit is owned by current player
        if not self.units.my_unit(a_unit.GetUID(), self.turns.CurrentPlayer()):
            print("{} is not your unit.".format(a_unit.GetUID()))
            return False
        # Make sure you're not attacking yourself.
        if self.units.my_unit(d_unit.GetUID(), self.turns.CurrentPlayer()):
            print("{} is your own unit. You cannot attack it.".format(d_unit.GetUID()))
            return False
        # Get attack multiplier based on Unit types
        u1_type = d_unit.GetType()
        u2_type = a_unit.GetType()
        atk_mult = self.attack_matrix.GetAttackMultiplier(u1_type, u2_type)
        # If unit1 was unable to defend remove from game
        if not d_unit.Defend(a_unit.GetHP(), atk_mult):
            self.units.del_unit(d_unit.GetUID())
            return True
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
