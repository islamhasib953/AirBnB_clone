#!/usr/bin/python3
"""
Class HBNBCommand
"""

import cmd
from models.base_model import BaseModel
from models.user import User
from models import storage
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State


class HBNBCommand(cmd.Cmd):
    data = ["BaseModel", "User", "Place", "State", "City", "Amenity", "Review"]
    attribute = ["id", "created_at", "updated_at"]
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

    def do_create(self, args):
        """
        Create New Instance Of class BaseModel
        and save it to the JSON file, and print the id
        """
        args = args.split()
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in HBNBCommand.data:
            print("** class doesn't exist **")
        else:
            new_instance = eval(args[0])()
            new_instance.save()
            print(new_instance.id)

    def do_show(self, args):
        """
        Prints the string representation of an instance based on the class name
        """
        args = args.split()
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in HBNBCommand.data:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        elif args[0] + "." + args[1] not in storage.all():
            print("** no instance found **")
        else:
            print(storage.all()[args[0] + "." + args[1]])

    def do_destroy(self, args):
        """
        Deletes an instance based on the
        class name and id (save the change into the JSON file).
        """
        args = args.split()
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in HBNBCommand.data:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        elif args[0] + "." + args[1] not in storage.all():
            print("** no instance found **")
        else:
            del storage.all()[args[0] + "." + args[1]]
            storage.save()

    def do_all(self, args):
        """
        Prints all string representation of
        all instances based or not on the class name.
        """
        args = args.split()
        if len(args) > 0 and args[0] not in HBNBCommand.data:
            print("** class doesn't exist **")
        else:
            for key, val in storage.all().items():
                print(str(val))

    def do_update(self, args):
        """
        Updates an instance based on the class name and id
        by adding or updating attribute (save the change into the JSON file).
        """
        args = args.split()
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in HBNBCommand.data:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        elif len(args) == 2:
            print("** attribute name missing **")
        elif len(args) == 3:
            print("** value missing **")
        else:
            if args[2] not in HBNBCommand.attribute:
                setattr(storage.all()[args[0] + "." + args[1]], args[2], args[3])
                storage.save()

    def default(self, line: str) -> None:
        line = line.split(".")
        if len(line) > 1:
            if line[1] == "all()":
                self.do_all(line[0])
            elif line[1] == "count()":
                sum = 0
                for key in storage.all():
                    if key.split(".")[0] == line[0]:
                        sum += 1
                print(sum)
            elif line[1].startswith("show"):
                new_line = line[1]
                start = new_line.find("(") + 2
                end = new_line.find(")") - 1
                new = new_line[start:end]
                self.do_show(line[0] + " " + new)
            elif line[1].startswith("destroy"):
                new_line = line[1]
                start = new_line.find("(") + 2
                end = new_line.find(")") - 1
                new = new_line[start:end]
                self.do_destroy(line[0] + " " + new)
            elif line[1].startswith("update"):
                line[1] = line[1].split(",")
                id = line[1][0][len('update("') : -1]
                name = line[1][1][1:-1]
                value = line[1][2][1:-2]
                self.do_update(line[0] + " " + id + " " + name + " " + value)


if __name__ == "__main__":
    HBNBCommand().cmdloop()
