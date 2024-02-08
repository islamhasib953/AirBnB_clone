#!/usr/bin/python3
"""
Class HBNBCommand
"""

import cmd
class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "
    """
    """
    def do_quit(self, args):
        """
        Quit command to exit the program
        """
        raise SystemExit
    
    def do_EQF(self, args):
        """
        EQF command to exit the program
        """
        return True
    
    def emptyline(self):
        """
        When enter emptyline should not be executed when imported
        """
        pass

if __name__ == "__main__":
    HBNBCommand().cmdloop()
