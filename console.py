#!/usr/bin/python3
""" Console Module """
import cmd
import sys
from models.base_model import BaseModel
from models.__init__ import storage
from models.engine.file_storage import FileStorage
from models.state import State
from models.city import City
from models.review import Review
from models.user import User
from models.amenity import Amenity
from models.place import Place


class HBNBCommand(cmd.Cmd):
    """Contains the functionality for the HBNB console"""
    # determines prompt for interactive/non-interactive modes
    prompt = '(hbnb)' if sys.__stdin__.isatty() else ''
    classes = {
            "BaseModel": BaseModel,
            "User": User,
            "State": State,
            "City": City,
            "Place": Place,
            "Amenity": Amenity,
            "Review": Review
        }

    def do_quit(self, arg):
        """Method to exit the HBNB console"""
        return True

    def help_quit(self):
        """Prints the help documentation for quit"""
        print("Quit command to exit the program")

    def do_EOF(self, arg):
        """Handles EOF to exit program"""
        return True

    def help_EOF(self):
        """Prints the help documentation for EOF"""
        print("Exits the program without formatting")

    def do_emptyline(self):
        """Overrides the emptyline method of CMD"""
        pass

    def help_emptyline(self):
        """Prints the help documentation for emptyline"""
        print("Overrides the emptyline method of CMD")

    def do_create(self, arg):
        """Creates a new instance of BaseModel"""
        if not arg:
            print("**class name missing**")
            return

        arg_list = arg.split()
        class_name = arg_list[0]

        if class_name not in HBNBCommand.classes:
            print("**class doesn't exist**")
            return

        for class_name, class_instance in HBNBCommand.classes.items():
            if class_name == arg:
                instance = class_instance()
                storage.save(instance)
            print(f"{instance.id}")
            break

    def help_create(self):
        """Prints the help documentation for create"""
        print("Creates a new instance of BaseModel")

    def do_show(self, arg):
        """Prints the string representation of an instance"""
        if not arg:
            print("**class name missing**")
            return
        else:
            args = arg.split()
            if args[0] not in HBNBCommand.classes:
                print("**class doesn't exist**")
            elif len(args) < 2:
                print("**instance id missing**")
            else:
                key = args[0] + " . " + args[1]
                new_dic = storage.all()
                if key in new_dic:
                    print(new_dic[key])
                else:
                    print("**no instance found**")

    def help_show(self):
        """Prints the help documentation for show"""
        print("Prints the string representation of an instance")

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id"""
        if not arg:
            print("**class name missing**")
        else:
            args = arg.split()
            if args[0] not in self.classes:
                print("**class doesn't exist**")
            elif len(args) < 2:
                print("**instance id missing**")
            else:
                key = args[0] + "." + args[1]
                new_dic = storage.all()
                if key in new_dic:
                    del new_dic[key]
                else:
                    print("**no instance found**")

    def help_destroy(self):
        """Prints the help documentation for destroy"""
        print("deletes an instance based on the class name and id")

    def do_all(self, arg):
        """Prints all string representation of all instances"""
        all_objects = storage.all()
        instances_list = []

        if not arg:
            for key, value in all_objects.items():
                instances_list.append(str(value))
        else:
            class_name = arg.split()[0]
            if class_name not in HBNBCommand.classes:
                print("** class doesn't exist **")
                return

            for key, value in all_objects.items():
                obj_class_name = key.split(".")[0]
                if obj_class_name == class_name:
                    instances_list.append(str(value))

        print(instances_list)

    def help_all(self):
        """Prints the help documentation for all"""
        print("Prints all string representation of all instances")

    def do_update(self):
        """Updates an instance based on the class name and id"""

    def help_update(self):
        """Prints the help documentation for update"""
        print("Updates an instance based on the class name and id")


if __name__ == "__main__":
    HBNBCommand().cmdloop()
