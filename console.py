#!/usr/bin/python3
""" Console Module """
import cmd
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
    prompt = '(hbnb)'

    classes = {
            "BaseModel": BaseModel,
            "User": User,
            "State": State,
            "City": City,
            "Place": Place,
            "Amenity": Amenity,
            "Review": Review
        }

    types = {
            'number_rooms': int, 'number_bathrooms': int, 
            'max_guest': int, 'price_by_night': int,
            'latitude': float, 'longitude': float
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

    def emptyline(self):
        """Overrides the emptyline method of CMD"""
        pass

    def help_emptyline(self):
        """Prints the help documentation for emptyline"""
        print("Overrides the emptyline method of CMD")

    def do_create(self, arg):
        """Creates a new instance of BaseModel"""
        if not arg:
            print("** class name missing **")
            return

        arg_list = arg.split()
        class_name = arg_list[0]
        instance = HBNBCommand.classes[class_name]()

        for ar in arg_list[1:]:
                name, value = ar.split('=')
                if value[0] == '\"':
                    value = value.replace('\"', '').replace('_', ' ')

                elif '.' in value:
                    value = float(value)

                else:
                    value = int(value)

                setattr(instance, name, value)

        if class_name not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return
        storage.save()
        instance.save()
        print(instance.id)
        storage.save()

    def help_create(self):
        """Prints the help documentation for create"""
        print("Creates a new instance of BaseModel")

    def do_show(self, arg):
        """Prints the string representation of an instance"""
        new = arg.partition(" ") 
        class_n = new[0]
        class_id = new[2]

        if class_id and ' ' in class_id:
            class_id = class_id.partition(' ')[0]
            

        if not class_n:
            print("** class name missing **")
            return

        if class_n not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return

        if not class_id:
            print("** instance id missing **")
            return
        
        key = class_n + "." + class_id
        
        try:
            print(storage._FileStorage__objects[key])
        except KeyError:
                print("** no instance found **")

    def help_show(self):
        """Prints the help documentation for show"""
        print("Prints the string representation of an instance")

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id"""
        if not arg:
            print("** class name missing **")
        else:
            arg = arg.split()
            if arg[0] not in self.classes:
                print("** class doesn't exist **")
            elif len(arg) < 2:
                print("** instance id missing **")
            else:
                key = arg[0] + "." + arg[1]
                new_dic = storage.all()
                if key in new_dic:
                    del new_dic[key]
                else:
                    print("** no instance found **")

    def help_destroy(self):
        """Prints the help documentation for destroy"""
        print("deletes an instance based on the class name and id")

    def do_all(self, arg):
        """Prints all string representation of all instances"""
        all_objects = storage.all()
        instances_list = []

        if not arg:
            for key, value in HBNBCommand.classes:
                instances_list.append(str(value))
        else:
            class_name = arg.split(' ')[0]
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

    def do_update(self, args):
        """Updates an instance based on the class name and id"""
        class_n = class_id = att_name = att_val = kwargs = '' 

        # individual cls from id/args
        args = args.partition(" ")
        if args[0]:
            class_n = args[0]
        else: # class name not present
            print("** class name missing **")
            return
        if class_n not in self.classes: # class name invalid
            print("** class doesn't exist **")
            return

        # individual id from args
        args = args[2].partition(" ")
        if args[0]:
            class_id = args[0]
        else: # id not present
            print("** instance id missing **")
            return

        key = class_n + "." + class_id

        if key not in storage.all():
            print("** no instance found **")
            return
        
        # determined kwargs or args
        if '{' in args[2] and '}' in args[2] and type(eval(args[2])) is dict:
            kwargs = eval(args[2])
            args = [] # reformat kwargs 
            for k, v in kwargs.items():
                args.append(k)
                args.append(v)
        else: # isolated args
            args = args[2]
            if args and args[0] == '\"': # check quoted arg
                second_quote = args.find('\"', 1)
                att_name = args[1:second_quote]
                args = args[second_quote + 1:]

            args = args.partition(' ')

            # if att_name not is quoted arg
            if not att_name and args[0] != ' ':
                att_name = args[0]
            # check for quoted val arg
            if args[2] and args[2][0] == '\"':
                att_val = args[2].partition(' ')[0]

            args = [att_name, att_val]

        # retrive dictionari of current objects
        new_dict = storage.all()[key]

        for i, att_name in enumerate(args):
            if (i % 2 == 0):
                att_val = args[i + 1]
            if not att_name:
                print("** attribute name missing **")
                return
            if not att_val:
                print("** value missing **")
                return
            
            # type cast
            if att_name in HBNBCommand.types:
                att_val = HBNBCommand.types[att_name](att_val)

            new_dict.__dict__.update({att_name: att_val})

        new_dict.save() # save updates to file

        

    def help_update(self):
        """Prints the help documentation for update"""
        print("Updates an instance based on the class name and id")


if __name__ == "__main__":
    HBNBCommand().cmdloop()
