
"""
Given a 2d array...
[
[1_, 2_, 3_, 2_, 1_],
[1x, 1x, 2x, 1x, 1_],
[1x, 1x, 5u, 2x, 1x],
[1x, 1x, 2x, 2_, 2_],
[1_, 1x, 2_, 2_, 1_]
]
where each value represents a movement cost.
Space u is never counted against movement ability
For example if unit exits at u with a movement ability of 3,
then u could move to spaces labeled with x.
"""

costMap1 = [
[1, 2, 3, 2, 1],
[1, 1, 2, 1, 1],
[1, 1, 5, 2, 1],
[1, 1, 2, 2, 2],
[1, 1, 2, 2, 1]]

costMap2 = [
[1, 2, 1, 2, 1],
[1, 1, 2, 1, 1],
[1, 2, 5, 2, 1],
[1, 1, 2, 1, 2],
[1, 1, 2, 2, 1]]

costMap3 = [
[2, 2, 2, 2, 2],
[2, 2, 2, 2, 2],
[2, 2, 5, 2, 2],
[2, 2, 2, 2, 2],
[2, 2, 2, 2, 2]]

costMap4 = [
[2, 2, 2, 2, 2],
[2, 2, 2, 2, 2],
[2, 1, 5, 1, 2],
[2, 2, 2, 2, 2],
[2, 2, 2, 2, 2]]

unitMovementAbility = 3
unitPosition = (2,2)
visitedSpaces = []

def print_map(a):
    for y in a:
        row = ""
        for x in y:
            row += "{} ".format(x)
        print row

def check_tile(costMap, pos):
    x, y = pos
    try:
        if x >= 0 and y >= 0:
            return costMap[y][x]
    except IndexError:
        pass
    return 999

def check_adjacent_tiles(costMap, pos, movCost):
    x, y = pos

    npos = (x, y+1)
    n = check_tile(costMap, npos )
    if n <= movCost:
        if not npos in visitedSpaces:
            visitedSpaces.append( npos )
        check_adjacent_tiles(costMap, npos, movCost - n )

    epos = (x+1, y)
    e = check_tile(costMap, epos )
    if e <= movCost:
        if not epos in visitedSpaces:
            visitedSpaces.append( epos )
        check_adjacent_tiles(costMap, epos, movCost - e )

    spos = (x, y-1)
    s = check_tile(costMap, spos )
    if s <= movCost:
        if not spos in visitedSpaces:
            visitedSpaces.append( spos )
        check_adjacent_tiles(costMap, spos, movCost - s )

    wpos = (x-1, y)
    w = check_tile(costMap, wpos )
    if w <= movCost:
        if not wpos in visitedSpaces:
            visitedSpaces.append( wpos )
        check_adjacent_tiles(costMap, wpos, movCost - w )
    return

def test():
    global costMap1
    global visitedSpaces

    print_map(costMap1)
    check_adjacent_tiles(costMap1, unitPosition, unitMovementAbility)
    print visitedSpaces
    visitedSpaces = []
    
    print_map(costMap2)
    check_adjacent_tiles(costMap2, unitPosition, unitMovementAbility)
    print visitedSpaces
    visitedSpaces = []
    
    print_map(costMap3)
    check_adjacent_tiles(costMap3, unitPosition, unitMovementAbility)
    print visitedSpaces
    visitedSpaces = []
    
    print_map(costMap4)
    check_adjacent_tiles(costMap4, unitPosition, unitMovementAbility)
    print visitedSpaces
    visitedSpaces = []
