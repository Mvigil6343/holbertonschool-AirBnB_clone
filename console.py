#!/usr/bin/python3
""" Console Module """
import cmd
import sys


class HBNBCommand(cmd.Cmd):
    """Contains the functionality for the HBNB console"""
    # determines prompt for interactive/non-interactive modes
    prompt = '(hbnb)' if sys.__stdin__.isatty() else ''

    def do_quit(self, command):
        """Method to exit the HBNB console"""
        exit()

    def help_quit(self):
        """Prints the help documentation for quit"""
        print("Exits the program with formatting")

    def do_EOF(self, arg):
        """Handles EOF to exit program"""
        exit()

    def help_EOF(self):
        """Prints the help documentation for EOF"""
        print("Exits the program without formatting")

    def do_emptyline(self):
        """Overrides the emptyline method of CMD"""
        pass

    def help_emptyline(self):
        """Prints the help documentation for emptyline"""
        print("Overrides the emptyline method of CMD")

    def do_create(self):
        """Creates a new instance of BaseModel"""

    def help_create(self):
        """Prints the help documentation for create"""
        print("Creates a new instance of BaseModel")

    def do_show(self):
        """Prints the string representation of an instance"""

    def help_show(self):
        """Prints the help documentation for show"""
        print("Prints the string representation of an instance")

    def do_destroy(self):
        """Deletes an instance based on the class name and id"""

    def help_destroy(self):
        """Prints the help documentation for destroy"""
        print("eletes an instance based on the class name and id")

    def do_all(self):
        """Prints all string representation of all instances"""

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
