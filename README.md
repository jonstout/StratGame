# StratGame

## Player
### fun GetPID(self)
Returns the player ID of this player.

## GameMap 
### fun ValidPosition(self, x, y)
Returns True if (x, y) is a valid position on this GameMap.

### GetNumberOfPlayers(self)
Returns the supported number of players on this GameMap.

### GetDefaultUnits(self)
Returns an array of the default units contained on this GameMap represented as a dict.

### GetDimensions(self)
Retruns the dimensions of this GameMap as a tuple in the form (GameMap.Width, GameMap.Height)
