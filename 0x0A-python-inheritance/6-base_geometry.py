#!/usr/bin/python3

"""An empty class"""


class BaseGeometry(object):
    """BaseGeometry is a class that serves as a template
    for creating custom objects.
    Public Methods:
    - area(self): Raises an exception indicating that the
    area() method is not implemented.
    """

    def area(self):
        """
        area(self):

        Raises an exception that the area() method is not implemented.
        """

        raise Exception("area() is not implemented")
