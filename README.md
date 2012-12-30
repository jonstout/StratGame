# StratGame

## Player
### func GetPID(self)
Returns the player ID of this player.

## GameMap 
### func ValidPosition(self, x, y)
Returns True if (x, y) is a valid position on this GameMap.

### func GetNumberOfPlayers(self)
Returns the supported number of players on this GameMap.

### func GetDefaultUnits(self)
Returns an array of the default units contained on this GameMap represented as a dict.

### func GetDimensions(self)
Retruns the dimensions of this GameMap as a tuple in the form (GameMap.Width, GameMap.Height)
