#!/usr/bin/python3
'''Module for command entry point'''
import cmd
import re
from shlex import split

import models
from models.base_model import BaseModel
from models.user import User

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

    def do_create(self, line):
        """creates new instance of base model"""
        if line == "" or line is None:
            print("** class name missing **")
        elif argv not in storage.classes():
            print("** class doesn't exist **")
        else:
            b = storage.classes()[line]()
            b.save()
            print(b.id)

    def do_show(self, line):
        """prints the string representation of instance"""
        if line == "" or line is None:
            print("** class name missing **")
        else:
            words = line.split(' ')
            if words[0] not in storage.classes():
                print("** class doesn't exist **")
            elif len(words) < 2:
                print("** instance is missing **")
            else:
                key = "{}.{}.format(args[0], args[1])"
                if key not in self.storage.all():
                    print("** no instance found **")
                else:
                    print(self.storage.all()[key])

      def do_destroy(self, line):
          """
          Deletes an instance based on the class name and id.
          """
          if line == "" or line is None:
              print("** class name missing **")
          else:
               words = line.split(' ')
               if words[0] not in storage.classes():
                   print("** class doesn't exist **")
               elif len(words) < 2:
                   print("** instance id missing **")
               else:
                   key = "{}.{}".format(words[0], words[1])
                   if key not in storage.all():
                        print("** no instance found **")
                    else:
                        del storage.all()[key]
                        storage.save()
    
    def do_all(self, lne):
        """
        prints all string rep. of instances
        """
         if line != "":
             words = line.spit(' ')
             if words[0] not in storage.classes():
                  print("** class doesn't exist **")
              else:
                   nl = [str(obj) for key, obj in storage.all().items()
                         if type(obj).__name__ == words[0]]
                   print(nl)
            else:
                 new_list = [str(obj) for key, obj in storage.all().items()]
                  print(new_list)

     def do_update(self, argv):
         """Updates an instance based on the class name and id"""
          arg_list = check_args(argv)
          if arg_list:
              if len(arg_list) == 1:
                  print("** instance id missing **")
              else:
                   instance_id = "{}.{}".format(arg_list[0], arg_list[1])
                    if instance_id in self.storage.all():
                        if len(arg_list) == 2:
                             print("** attribute name missing **")
                         elif len(arg_list) == 3:
                             print("** value missing **")
                         else:
                             obj = self.storage.all()[instance_id]
                             if arg_list[2] in type(obj).__dict__:
                                  v_type = type(obj.__class__.__dict__[arg_list[2]])
                                  setattr(obj, arg_list[2], v_type(arg_list[3]))
                              else:
                                   setattr(obj, arg_list[2], arg_list[3])
                    else:
                         print("** no instance found **")
                self.storage.save()




if __name__ == '__main__':
    HBNBCommand().cmdloop()
