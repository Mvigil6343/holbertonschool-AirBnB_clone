#!/usr/bin/python3
"""Class that serializes and deserializes JSON file to instances"""
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review


class FileStorage:
    """class that handles serialization and deserialization"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """method that returns the dictionary <__objects>"""
        return self.__objects

    def new(self, obj):
        """method that sets in <__objects> the object <obj>"""
        new_obj = obj.__class__.__name__
        self.__objects["{}.{}".format(new_obj, obj.id)] = obj

    def save(self, arg):
        """method that serializes <__objects> to a JSON file"""
        serialized_objs = {}
        for key, obj in self.__objects.items():
            serialized_objs[key] = obj.to_dict()

        with open(self.__file_path, 'w') as f:
            json.dump(serialized_objs, f, indent=4)

    def reload(self):
        """method that deserializes the JSON file to __objects"""
        classes = {
            "BaseModel": BaseModel,
            "User": User,
            "State": State,
            "City": City,
            "Place": Place,
            "Amenity": Amenity,
            "Review": Review
        }
        try:
            with open(FileStorage.__file_path, 'r') as f:
                serialized_objs = json.load(f)
                for v in serialized_objs.values():
                    classname = v["__class__"]
                    self.new(classes[classname](**v))

        except FileNotFoundError:
            pass
