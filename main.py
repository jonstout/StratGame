# @author Jonathan Stout

from cli import Cli

if __name__ == "__main__":
    game = Cli("./config.json")
    game.Run()