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


    def integer_validator(self, name, value):
        """
        integer_validator(self, name, value)

        Validates that the value is an integer and meets certain conditions.

        Parameters:
        - name (str): The name of the variable being validated.
        - value: The value to be validated.

        Raises:
        - TypeError: If the value is not an integer.
        - ValueError: If the value is less than or equal to 0.
        """
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")

        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
