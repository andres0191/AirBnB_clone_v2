#!/usr/bin/python3
"""This is the file storage class for AirBnB"""

#  ███████╗    ███████╗████████╗ ██████╗ ██████╗  █████╗  ██████╗ ███████╗
#  ██╔════╝    ██╔════╝╚══██╔══╝██╔═══██╗██╔══██╗██╔══██╗██╔════╝ ██╔════╝
#  █████╗      ███████╗   ██║   ██║   ██║██████╔╝███████║██║  ███╗█████╗
#  ██╔══╝      ╚════██║   ██║   ██║   ██║██╔══██╗██╔══██║██║   ██║██╔══╝
#  ██║██╗      ███████║   ██║   ╚██████╔╝██║  ██║██║  ██║╚██████╔╝███████╗
#  ╚═╝╚═╝      ╚══════╝   ╚═╝    ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝ ╚══════╝


import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class FileStorage:
    """This class serializes instances to a JSON file and
    deserializes JSON file to instances
    Attributes:
        __file_path: path to the JSON file
        __objects: objects will be stored
    """
    __file_path = "file.json"
    __objects = {}

    def all(self, cls=None):
        """returns a dictionary
        Return:
            returns a dictionary of __object
            check cast of string "State" and State
        """
        if cls is None:
            return self.__objects

        class_name = cls.__name__

        new_dict = {}

        for key, val in self.__objects.items():

            if class_name in key:
                new_dict[key] = val

        return new_dict

    def new(self, obj):
        """sets __object to given obj
        Args:
            obj: given object
        """
        if obj:
            key = "{}.{}".format(type(obj).__name__, obj.id)
            self.__objects[key] = obj

    def save(self):
        """serialize the file path to JSON file path
        """
        my_dict = {}
        for key, value in self.__objects.items():
            my_dict[key] = value.to_dict()
        with open(self.__file_path, 'w', encoding="UTF-8") as f:
            json.dump(my_dict, f)

    def reload(self):
        """serialize the file path to JSON file path
        """
        try:
            with open(self.__file_path, 'r', encoding="UTF-8") as f:
                for key, value in (json.load(f)).items():
                    value = eval(value["__class__"])(**value)
                    self.__objects[key] = value
        except FileNotFoundError:
            pass

    def delete(self, obj=None):
        """
            delete obj from __opbjects
        """
        if obj:
            class_name = obj.__class__.__name__
            key_dict = class_name + "." + obj.id
            del self.__objects[key_dict]
            self.save()

    def close(self):
        """ Add a public method def close(self)::
            call reload() method for deserializing
            the JSON file to objects
        """
        self.reload()
