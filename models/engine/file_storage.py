#!/usr/bin/python3
"""Class that serializes JSON file to instances"""
import json
from models.base_model import BaseModel


class FileStorage:
    """Class that handles serialization and deserialization"""
    _file_path = "file.json"
    _objects = {}

    def all(self):
        """Method that returns the dictionary <_objects>"""
        return self._objects
    
    def new(self, obj):
        """method that sets in <_objects> the object <obj>"""
        self._objects[f"{type(obj)._name_}.{obj.id}"] = obj
    
    def save(self):
        """Method that serializes <_objects> to a JSON file"""
        
    def reload(self):
        """Method that deserializes the JSON file to _objects"""
