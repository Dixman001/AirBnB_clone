#!/usr/bin/python3
'''Module for command entry point'''
import cmd
import re
from shlex import split

import models
from models.base_model import BaseModel

class HBNBCommand(cmd.Cmd):
    """
    console implementation for
    the airBnB clone
    """
    prompt = "(hbnb) "
    storage = models.storage

    def emptyline(self):
        """command to execute empty line"""
        pass
    
    def do_EOF(self, argv):
        """to exit the program"""
        return True

    def do_quit(self, argv):
        """to exit the console"""
        return True


if __name__ == '__main__':
    HBNBCommand().cmdloop()
