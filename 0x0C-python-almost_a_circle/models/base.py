#!/usr/bin/python3
"""Defining a class base"""


class Base:
    """
    Base class to manage id attribute for all future classes in the project.

    Attributes:
        __nb_objects (int): Private class attribute.
        id (int): Public instance attribute represent the unique
        identifier for each instance.

    Methods:
        __init__(self, id=None): Class constructor to initialize id attribute.
    """
    __nb_objects = 0
    """
        Initialize Base instance with a unique identifier.

        Args:
            id (int, optional): Identifier for the instance.
        """
    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
