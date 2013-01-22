# @author Jonathan Stout

import string

from model.game_map import GameMap
from model.player import Player
from model.turns import Turns
from model.unit import Unit
from model.unitmanager import UnitManager
from model.configuration import Configuration
from model.buildingmanager import BuildingManager

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
    def __init__(self, config):
        self.config = Configuration(config)
        self.turns = Turns()

        self.game_map = None
        self.units = None
        self.buildings = None
        self.game_on = True

    def get_gamemaps(self):
        maps = self.config.GetGamemaps()
        for m in maps:
            yield (m, maps[m])

    def load_gamemap(self, _id):
        self.game_map = GameMap(self.config.GetGamemapSource(_id))

        game_units = self.game_map.GetDefaultUnits()
        self.units = UnitManager()
        for player_id in game_units:
            self.turns.AddPlayer( int(player_id) )
            for unit in game_units[player_id]:
                self.units.add_unit(unit, int(player_id))

        game_buildings = self.game_map.GetBuildings()
        self.buildings = BuildingManager(self.config.GetBuildingsConfig())
        for player_id in game_buildings:
            for build in game_buildings[player_id]:
                self.buildings.add_building(build, int(player_id))
        return True

    def end_game(self):
        self.game_on = False

    def game_over(self):
        return not self.game_on

    def get_current_player(self):
        return self.turns.CurrentPlayer()

    def next_player(self):
        return self.turns.NextPlayer()

    def ListBuildings(self):
        result = self.buildings.get_buildings()
        for b in result:
            yield result[b]

    def ListUnits(self):
        """
        Lists all units in the game. Of course you can only use
        your game units.
        """
        for u in self.units.get_units():
            print u
    
    def MoveUnit(self, uid, pos):
        """
        Moves a unit if the movement is valid. Returns True if a
        valid move; Else False.
        """
        if self.units.my_unit(uid, self.turns.CurrentPlayer()) and \
                self.game_map.ValidPosition(pos[0], pos[1]):
            return self.units.move_unit(uid, pos)
        return False

    def my_unit(self, uid):
        return self.units.my_unit(uid, self.turns.CurrentPlayer())

    def AttackUnit(self, dunit, aunit):
        d_unit = self.units.get_unit(dunit)
        a_unit = self.units.get_unit(aunit)
        # Get attack multiplier based on Unit types
        u1_type = d_unit.GetType()
        u2_type = a_unit.GetType()
        atk_mult = self.config.GetAttackMultiplier(u1_type, u2_type)
        # If unit1 was unable to defend remove from game
        battle_res = d_unit.Defend(a_unit.GetHP(), atk_mult)
        if battle_res[0] <= 0:
            self.units.del_unit(d_unit.GetUID())
        return battle_res
