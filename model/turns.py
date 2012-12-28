# PlayersTurn
#
#

class Turns(object):
    """ Turns
    Track whose turn it is and turn counts.
    """
    def __init__(self):
        """ __init__
        """
        self.total_turns = 0
        self.players = []

    def AddPlayer(self, player_id):
        """ AddPlayer
        Adds a player_id to self.players.
        """
        self.players.append(player_id)

    def CurrentPlayer(self):
        """ CurrentPlayer
        Returns : The player_id of the current player.
        """
        index = self.total_turns % len(self.players)
        return self.players[index]

    def NextPlayer(self):
        """ NextPlayer
        Returns : The player_id of the next player.
        """
        self.total_turns += 1
        index = self.total_turns % len(self.players)
        return self.players[index]

    def FullTurns(self):
        """ FullTurns
        Returns : The number of full turns (Each player has played
        an equal number of times).
        """
        return self.total_turns / len(self.players)

    def TotalTurns(self):
        """ TotalTurns
        Returns : The total number of turns played.
        """
        return self.total_turns
