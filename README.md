## Player Actions

move_unit u_id x y

attack_unit du_id au_id

cap_building b_id u_id

## Needed calls

unit_mine? u_id

## Game

### func AttackUnit(defUnitID, atkUnitID)
Attacks defUnitID with atkUnitID. Returns True if the unit was destroyed, and False if not.

### func ListUnits
Returns a list of units with properties HP, ID, Position, and Type.

### func MoveUnit(unit_id, position)
Move a unit. Returns True if unit can be moved, and False if not.

### func Done
Called when a player ends his or her turn.

### func ListBuildings
Returns a list of buildings with properties OwnerID, 

- hp
- owner
- position
- type
- uID

get_buildings
- captured
- capture_cost
- bID
- owner
- position
- type

get_tiles
- movement_cost
- position
- type
