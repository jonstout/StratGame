# @author Jonathan Stout

from model.game import Game
import string

class Cli(object):
    def __init__(self, config):
        # Build a Game object based on config
        self.game = Game(config)

    def Run(self):
        self.select_gamemap()
        while not self.game.game_over():
            print("It's Player {}'s turn.".format(self.game.get_current_player()))
            raw = raw_input("$ ")
            cmd = string.split(raw, " ")

            if cmd[0] == "exit":
                self.game.end_game()
            elif cmd == "help":
                print("exit - End program")
                print("help - Print this help message")
                print("list_units - List available units and their location")
                print("attack_unit <u1> <u2> - Attack unit u1 with unit u2")
                print("move_unit <u1> <x>.<y> - Move unit u1 to position (x, y)")
                print("done - End player's turn")
            elif cmd[0] == "list_units":
                self.game.ListUnits()
            elif cmd[0] == "move_unit":
                args = self.move_unit(cmd)
                self.game.MoveUnit(args[0], args[1])
            elif cmd[0] == "attack_unit":
                args = self.attack_unit(cmd)
                if not self.game.my_unit(args[1]):
                    print("{} is not your unit to attack with.".format(args[1]))
                elif self.game.my_unit(args[0]):
                    print("{} is your own unit. You cannot attack it.".format(args[0]))
                else:
                    results = self.game.AttackUnit(args[0], args[1])
                    if results[0] <= 0:
                        print("Unit {} was destroyed.".format(args[0]))
                    else:
                        print("Unit {}: {}HP, Unit {}: {}HP".format(args[0],results[0],args[1],results[1]))
            elif cmd[0] == "done":
                print("Player{}'s turn is over.".format(self.game.get_current_player()))
                self.game.next_player()
            else:
                print("Bad command")
        # Game loop has been broken by exit command
        print("Game Over")

    def attack_unit(self, cmd):
        d_unit = int(cmd[1])
        a_unit = int(cmd[2])
        return (d_unit, a_unit)

    def move_unit(self, cmd):
        uid = int(cmd[1])
        pos = string.split(cmd[2], ".")
        pos[0] = int(pos[0])
        pos[1] = int(pos[1])
        return (uid, pos)

    def select_gamemap(self):
        gamemaps = self.game.get_gamemaps()
        
        print("Select a Map...")
        for _map in gamemaps:
            print(_map)

        while True:
            raw = raw_input("$ ")
            cmd = string.split(raw, " ")
            if self.game.load_gamemap(cmd[0]):
                break
