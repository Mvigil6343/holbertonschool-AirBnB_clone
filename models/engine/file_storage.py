#!/usr/bin/python3
"""Class that serializes and deserializes JSON file to instances"""
import json


class FileStorage:
    """class that handles serialization and deserialization"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """method that returns the dictionary <__objects>"""
        return self.__objects

    def new(self, obj):
        """method that sets in <__objects> the object <obj>"""
        self.__objects[f"{type(obj).__name__}.{obj.id}"] = obj

    def save(self):
        """method that serializes <__objects> to a JSON file"""
        serialized_objs = {}
        for key, obj in self.__objects.items():
            serialized_objs[key] = obj.to_dict()

        with open(self.__file_path, 'w') as f:
            json.dump(serialized_objs, f)

    def reload(self):
        """method that deserializes the JSON file to __objects"""
