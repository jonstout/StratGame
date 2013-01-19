## Game

### func AttackBuilding(defBuildID, atkUnitID)
Attacks (captures) defBuildID with atkUnitID. Returns True if the building was captured, and defBuildID's remaining cost to capture if not.

### func AttackUnit(defUnitID, atkUnitID)
Attacks defUnitID with atkUnitID. Returns True if the unit was destroyed, and False if not.

### func ListBuildings
Returns a list of buildings with properties ID, OwnerID, CaptureCost, Position, Type

### func ListGameTiles
Returns a list of game tiles with properties MovementCost, Position, Type

### func ListUnits
Returns a list of units with properties HP, ID, OwnerID, Position, and Type.

### func MoveUnit(unit_id, position)
Move a unit. Returns True if unit can be moved, and False if not.

### func Done
Called when a player ends his or her turn.
